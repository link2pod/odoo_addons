from odoo import http
from odoo.http import request, route, Response

"""
class OwlPlayground(http.Controller):
    @http.route(['/owl_playground/playground'], type='http', auth='public')
    def show_playground(self):
        Renders the owl playground page
        return request.render('owl_playground.playground')
        """

# Render root website pages  (i.e. GET request to /dashboard)
class SolidDashboard(http.Controller):
    @http.route(['/my/solid-dashboard'], type='http', auth='public', website=True)
    def show_dashboard(self):
        qcontext = request.params.copy()
        return request.render('solid.dashboard_page')

    @http.route(['/my/subscription'], type='http', auth='public', website=True)
    def show_subscription(self):
        qcontext = request.params.copy()
        return request.render('solid.subscription_page')
    



    


