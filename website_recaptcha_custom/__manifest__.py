# Copyright 2021 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website reCAPTCHA Login/Signup/Contactus',
    'category': 'website',
    'version': '14.0.1',

    'summary': 'Website reCAPTCHA Login/Signup/Contactus',

    'description': """
    Website reCAPTCHA Login/Signup/Contactus
        """,

    'author': 'Odoo Helper',
    'license': 'AGPL-3',

    'depends': ['base', 'website', 'website_crm', 'auth_signup'],
    'data': [
        'views/template.xml',
    ],

    'images': ['images/OdooHelper.jpg'],

    'price': 22.17,
    'currency': 'USD',

    'installable': True,
    'application': False
}
