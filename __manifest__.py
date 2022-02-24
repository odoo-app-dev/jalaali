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
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
    'web._assets_common_scripts': [
    'jalaali/static/js/moment-jalaali.js',
    'jalaali/static/js/tempusdominus_fixed.js',
    'jalaali/static/js/fullcalendar_fixed.js',
    'jalaali/static/js/mytime.js',
    ],
    'web.tests_assets': [
    'jalaali/static/js/daterangepicker_fixed.js',
    ],
    },
    # 'web._assets_common_scripts': [
    # 'web/static/lib/moment/moment-jalaali.js',
    # 'web/static/lib/tempusdominus/tempusdominus_fixed.js',
    # 'web/static/src/legacy/js/libs/fullcalendar_fixed.js',
    # 'web/static/src/legacy/js/core/mytime.js',
    # ],
}
