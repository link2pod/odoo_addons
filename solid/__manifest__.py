# -*- coding: utf-8 -*-
{
    'name': "solid",

    'summary': """
        Link your database to your solid server. 
        """,

    'description': """
        Link your database to your solid server. 
        Add's a web_id field to the res.users model. 
        Integrate webId creation from a solid server to the form at /web/signup.
    """,

    'author': "Link2.ca",
    'website': "https://www.link2.ca",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'auth_signup','portal'],
    'application': True,
    'installable': True,
    'data': [
         'views/templates.xml',
        'views/portal.xml',
        # overrides auth_signup.fields
         'views/signup_view.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'solid/static/src/**/*',
        ],
    }
}
