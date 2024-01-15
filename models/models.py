# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


# class OdooJalaali(models.Model):
#     _inherit = 'res.users'
#
#     fonts = fields.Selection([('none', _('None')), ('iran_sans_fn', 'IRANSansFN')], default='none')
#
#     def get_user_preferred_font(self):
#         return