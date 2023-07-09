from odoo import http, _
from odoo.http import request, route,Response
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.addons.auth_signup.models.res_users import SignupError
from odoo.addons.web.controllers.home import SIGN_UP_REQUEST_PARAMS
import requests
import werkzeug

'''
parameter used for login/signup
Refer to https://github.com/odoo/odoo/blob/16.0/addons/web/controllers/home.py#L22
'''
SIGN_UP_REQUEST_PARAMS.add('web_id')  # web-id not web_id because odoo convention model_id 
SIGN_UP_REQUEST_PARAMS.add('podName') 



'''
Extends the AuthSignupHome Controller (https://github.com/odoo/odoo/blob/d15d716801ddc01990016ab9461109c044ea497f/addons/auth_signup/controllers/main.py)
so that the web_auth_signup handler for '/web/signup' (https://github.com/odoo/odoo/blob/d15d716801ddc01990016ab9461109c044ea497f/addons/auth_signup/controllers/main.py#L36)
- creates a web_id in the solid-server (for this example
    the server is https://solidserver.southafricanorth.cloudapp.azure.com/)
- adds the web_id to the corresponding field in res.users.web_id (from extended model 
    SolidResUser class which inherits res.users)
'''
class ExtensionAuthSignupHome(AuthSignupHome):

    # override do_signup(self, qcontext)
    def do_signup(self, qcontext):
        print("in dosignup")
        ''' Overall process:
        Step 1: Create WebID for user on a solid server
        Step 2: Create Record on the Odoo database for res.partners
        '''
        web_id = self.register_web_id(qcontext=qcontext)
        #print("webId", webId) #debug
        qcontext['webId']=web_id
        #print("new qcontext",qcontext)
        
        """ Signup with values. Adapted from original do_signup code: https://github.com/odoo/odoo/blob/91f970fdfd8136e303b7052d690d8997f0278f24/addons/auth_signup/controllers/main.py#L150C35-L154C32 """
        values = self._prepare_signup_values(qcontext)
        values['web_id'] = web_id # New: Add webId to values used to signup
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()

    # registers a web_id at a solid-server with data from qcontext
    def register_web_id(self, qcontext):
        # api endpoint to register a webID on a solid server
        # TODO move endpoint into environment variable
        #register_endpoint = 'https://solidserver.southafricanorth.cloudapp.azure.com/idp/register/'
        #register_endpoint = 'https://solidserver.southafricanorth.cloudapp.azure.com/idp/register/'
        #register_endpoint = 'http://localhost:8000/idp/register/'
        base_server_url = 'http://172.17.0.4:8000/'
        register_endpoint = base_server_url+'idp/register/'
        credentials_endpoint = base_server_url+'idp/credentials/'
        

        print("in register_web_id")
        # Check if account with email already exists
        credential_result = requests.post(
            url=credentials_endpoint,
            json={
                'email': qcontext['login'],
                'password': '\n',
            }
        )
        print("credentials", credential_result, credential_result.content) #debugging purposes

        if (credential_result.status_code == 200 
            or credential_result.json()['message'] == 'Incorrect password'
        ):
            #qcontext["error"] = _("Another user is already registered using this email address.")
            # TODO: implement better error message
            raise SignupError(_("Email already exists"))
        
        # otherwise, try creating web_id with data from signup form 
        # Rename qcontext keys to conform to solid server 
        values = qcontext
        values['email'] = values['login']
        values['confirmPassword'] = values['confirm_password']
        values['createWebId'] = True
        values['createPod'] = True
        values['register'] = True
        
        print("values", values) #debugging purposes
        register_result = requests.post(
            url=register_endpoint,
            json=values,
        )

        print("register result:", register_result, register_result.content) # Debugging

        # Handle potential errors when creating webID
        if (register_result.status_code!=200): 
            message = register_result.json()['message']
            if (message == 'There already is an account for this WebID'):
                message = 'Pod Name is already taken' # above message translates to podName taken
            qcontext['error'] = _(message) #TODO: show error in frontend UI
            
            raise SignupError(_(message))
        register_result_json = register_result.json()
        print("content json", register_result_json) #debug
        
        web_id = register_result_json['webId']
        #webId = "http://somewhere/test/profile/card#me"
        return web_id








