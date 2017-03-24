# -*- coding: utf-8 -*-

{
    'name': 'Delivery Order Line Number',
    'version': '9.0.1.1.0',
    'category': 'Tools',
    'sequence': 14,
    'author': 'KJK meisterHONEN - Michael Sachin',
    'website': 'www.meisterhonen.com',
    'summary': """Delivery Order Line Number""",
    'description': """Line Numbers in delivery orders / delivery Challan - This module creates a field called number.
                      You will have to manually include this in your report - Contact if you need support!""",
    'license': 'Other proprietary',
    'images': ['static/description/icon.png'],
    'depends': [
        'stock',
    ],
    'data': [
        'view/delivery_order_view.xml'
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 5,
    'currency': 'EUR',
}
