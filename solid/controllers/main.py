from odoo import http
from odoo.http import request, route, Response

# Render root website pages  (i.e. GET request to /solid/playground, /signup)

class SolidPlayground(http.Controller):
    """ Renders the owl playground page """
    @http.route(['/solid/playground'], type='http', auth='public')
    def show_playground(self):
        return request.render('solid.playground')
    
    """ Renders the signup page """
    @http.route(['/signup'], type='http', auth='public')
    def show_signup_page(self):
        #return Response(status=200,response="working")
        return request.render('solid.signup_page')

    


