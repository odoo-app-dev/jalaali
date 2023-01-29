# -*- coding: utf-8 -*-
{
    'name': "jalaali",

    'summary': """
        It will show the jalaali date for most of date fields""",

    'description': """
        
    """,

    'author': "Arash Homayounfar",
    'website': "https://karvazendegi.com/odoo",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Service Desk/Service Desk',
    'application': False,
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        ],
    'assets': {
        'web.assets_backend': [
            'jalaali/static/js/mytime.js',
            'jalaali/static/js/moment-jalaali.js',
            'jalaali/static/js/daterangepicker_fixed.js',
            'jalaali/static/js/tempusdominus_fixed.js',
            # 'jalaali/static/js/fullcalendar_fixed.js',
            ],
        },
    'license': 'LGPL-3',
}
