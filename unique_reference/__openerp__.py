# -*- coding: utf-8 -*-
{
    'name': "Unique Internal Reference / default_code Field",

    'summary': """
        Unique Internal Reference code for Products - 
        with existing code backup ( Einzigartig Interne Referenz Mit Sicherung )""",

    'description': """
        This module checks to make sure, the Internal Reference field in products is Unique.
        It includes an Alert! message when you enter a code that already exists.
        Does your Internal Reference field disappear when you update product attributes or values?
        This module also saves a backup of the Existing Internal Reference, so you can just copy it
        from the field below.
    """,

    'author': "Michael Sachin",
    'category': 'Tools',
    'version': '0.1',
    'licence': 'Other proprietary',
    'depends': ['sale'],
    'data': [
        'views/unique_reference_view.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 15.00,
    'currency': 'USD'
}
