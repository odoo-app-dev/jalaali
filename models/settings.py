# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from colorama import Fore
import pytz


# #################################################################################################
class OdooJalaaliSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    language_font = fields.Selection([('none', _('None')), ('iran_sans_fn', 'IRANSansFN')], default='none',
                                     config_parameter='base_setup.language_font')


    def get_language_font(self):
        return self.env['ir.config_parameter'].sudo().get_param('base_setup.language_font', default=0)

