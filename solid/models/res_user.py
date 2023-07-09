from odoo import models,fields,api

# Extend user to include a web_id field
class SolidResUser(models.Model):
    _inherit = 'res.users'
    
    # string representing URL of the user's webID
    # Sorry for confusion with Odoo conventions
    web_id = fields.Char(
        string='Solid Web Id',
    )

    @api.model
    def create(self,vals):
        # Create parent res.user record
        user_id = super(SolidResUser, self).create(vals)
        # Set the webID (if given in parameter vals) 
        if (vals['web_id']):
            user_id.web_id = vals['web_id']
        
        return user_id


