# -*- coding: utf-8 -*-
{
    'name': "Auto Custom Description for Quotation and Sale Order",

    'summary': """
        Generate Customized Description for Quotations and Sale Orders Automatically""",

    'description': """
        This module Generates the Description for Quotations and Sale Orders based on the 'Attribute Values' of your chosen 'Product Attributes'.
        Do you spend much "Man hours" on a regular basis to prepare the description for every product you create?
        Well, this module automates this process.
    """,

    'author': "Michael Sachin",
    'category': 'Productivity',
    'version': '0.1',
    'licence': 'Other proprietary',
    'depends': ['sale'],
    'data': [
        'views/sale_desc_view.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 99.00,
    'currency': 'EUR'
}
