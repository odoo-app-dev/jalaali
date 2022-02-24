# -*- coding: utf-8 -*-
# from odoo import http


# class Jalaali(http.Controller):
#     @http.route('/jalaali/jalaali/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jalaali/jalaali/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jalaali.listing', {
#             'root': '/jalaali/jalaali',
#             'objects': http.request.env['jalaali.jalaali'].search([]),
#         })

#     @http.route('/jalaali/jalaali/objects/<model("jalaali.jalaali"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jalaali.object', {
#             'object': obj
#         })
