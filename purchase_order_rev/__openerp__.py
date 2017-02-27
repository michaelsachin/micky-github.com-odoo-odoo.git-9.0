# -*- coding: utf-8 -*-
##############################################################################
#    Purchase Order Revision
##############################################################################

{
    'name': "Purchase order revision",
    'category': 'Tools',
    'version': '1.0',
    'author': 'Michael Sachin',
    'licence': 'Other proprietary',
    'website': 'http://www.odoo.com',
    'summary': """Revise Purchase Orders.""",
    'description': """Revise Purchase Orders.""",
    'depends': ['purchase'],
    "data": [
        'views/purchase_view.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 29.00,
    'currency': 'USD',
}



