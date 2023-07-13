from odoo.addons.portal.controllers.portal import CustomerPortal 
import logging
_solid_logger = logging.getLogger(__name__)

class ExtendCustomerPortal(CustomerPortal):
    # override Not working for some reason
    def _prepare_home_portal_values(self, counters):
        values = super(ExtendCustomerPortal, self)._prepare_home_portal_values(counters)
        usage_count = 1
        subscription_count = 1
        values['usage_count'] = usage_count,
        values['subscription_count'] = subscription_count,
        _solid_logger.info("values %s", values) # not working for some reason
        return values
    
    
