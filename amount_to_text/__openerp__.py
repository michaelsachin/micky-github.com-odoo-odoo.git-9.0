# -*- coding: utf-8 -*-
##############################################################################
#   KJK meisterHONEN
##############################################################################

{
    'name' : 'Amount in words',
    'version' : '1.0',
    'author' : 'KJKmH - Michael Sachin',
    'summary': 'Amount in Words without Euro or Cents',
    'description': """Amount in Words for Invoice.
                      Example - Rs 1386.41 is translated as 'One Thousand, Three Hundered Eighty-Six Only'
                      Field to add in your report - <span t-field="o.currency_id"/> <span t-esc="o.amount_to_text(o.amount_total, o.currency_id)"/>
    """,
    'category': 'Localization',
    'sequence': 4,
    'website' : 'http://www.meisterhonen.com',
    'licence': 'Other Proprietary',
    'images': ['static/description/icon.png'],
    'depends' : ['account', 'report'],
    'demo' : [],
    'data' : [
        'views.xml',
    ],
    'auto_install': False,
    'application': False,
    'installable': True,
    'price': 9,
    'currency': 'EUR',
}

#im:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
