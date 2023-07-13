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
    'website': "https://link2.ca",

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
        'solid.assets_dashboard': [
            # bootstrap
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap'),

            'web/static/src/libs/fontawesome/css/font-awesome.css', # required for fa icons
            'web/static/src/legacy/js/promise_extension.js', # required by boot.js
            'web/static/src/boot.js', # odoo module system
            'web/static/src/env.js', # required for services
            'web/static/src/session.js', # expose __session_info__ containing server information
            'web/static/lib/owl/owl.js', # owl library
            'web/static/lib/owl/odoo_module.js', # to be able to import "@odoo/owl"
            'web/static/src/core/utils/functions.js',
            'web/static/src/core/browser/browser.js',
            'web/static/src/core/registry.js',
            'web/static/src/core/assets.js',
            'web/static/src/search/layout.js',
            'solid/static/src/**/*',
        ],
    }
}
