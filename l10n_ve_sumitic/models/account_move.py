# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_ve_taxpayer_type = fields.Selection([
        ('res_re', 'Persona Natural Residente'),
        ('res_nr', 'Persona Natural No Residente'),
        ('dom_re', 'Persona Jurídica Domiciliada'),
        ('dom_nr', 'Persona Jurídica No Domiciliada'),
    ], string='Tipo de Contribuyente', help='Tipo de contribuyente para la localización venezolana')
