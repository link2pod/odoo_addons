from odoo import http
from odoo.http import request, route, Response
import logging
_solid_logger = logging.getLogger(__name__)

"""
class OwlPlayground(http.Controller):
    @http.route(['/owl_playground/playground'], type='http', auth='public')
    def show_playground(self):
        Renders the owl playground page
        return request.render('owl_playground.playground')
        """

# Render root website pages  (i.e. GET request to /dashboard)
class SolidDashboard(http.Controller):
    @http.route(['/my/solid-dashboard'], type='http', auth='user', website=True)
    def show_dashboard(self):
        qcontext = request.params.copy()
        _solid_logger.debug("request.env: ")
        for i in request.env: 
            _solid_logger.debug("%s", i)
        _solid_logger.debug("web_id:%s, login:%s", request.env.user.web_id, request.env.user.login)
        user = request.env.user
        web_id = user.web_id
        return request.render('solid.dashboard_page', {
            'user': user,
            'web_id': user.web_id,
        })

    @http.route(['/my/subscription'], type='http', auth='public', website=True)
    def show_subscription(self):
        qcontext = request.params.copy()
        return request.render('solid.subscription_page')

    @http.route('/my/statistics', type='json', auth='user')
    def get_statistics(self):
        user_id = request.env.context.get('uid')

        _solid_logger.debug("request.env: %s, user_id: %s", request.env, user_id)

        

        result = {
            "web_id": request.env.user.web_id,
        }

        return result
    



    


