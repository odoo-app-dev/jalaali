# -*- coding: utf-8 -*-
{
    'name': "odoo_jalaali",

    'summary': """
        It will show the jalaali date for most of date fields""",

    'description': """
        
    """,

    'author': "Arash Homayounfar",
    'website': "https://gilaneh.com/shop/odoo-jalaali-date-1",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Service Desk/Service Desk',
    'application': False,
    'version': '1.2.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/settings.xml',
        ],
    'assets': {
        'web._assets_common_scripts': [
            'odoo_jalaali/static/js/jalaali.js',
            'odoo_jalaali/static/js/moment/moment-jalaali.js',
            'odoo_jalaali/static/js/tempusdominus/tempusdominus_fixed.js',
            'odoo_jalaali/static/js/language_font_backend.js',

        ],
        'web._assets_common_styles': [
            'odoo_jalaali/static/css/fonts.scss',

        ],
        'web.assets_backend': [
            # 'odoo_jalaali/static/js/language_font.js',

            # ('replace', 'web/static/src/legacy/js/components/datepicker.js', 'odoo_jalaali/static/js/datepicker/datepicker_fixed.js'),
            ],
        'web.assets_frontend': [
            # 'odoo_jalaali/static/js/jalaali_class.js',
            'odoo_jalaali/static/js/language_font_frontend.js',

            'odoo_jalaali/static/css/fonts.scss',
            ],
        'web.report_assets_common': [
            # 'odoo_jalaali/static/js/jalaali_class.js',
            'odoo_jalaali/static/css/fonts.scss',
            ],
        },
    'license': 'LGPL-3',
}
