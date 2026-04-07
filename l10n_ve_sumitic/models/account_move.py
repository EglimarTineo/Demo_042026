# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    # Campo para el número de control (requerido en Venezuela)
    l10n_ve_control_number = fields.Char(
        string='Número de Control',
        copy=False,
        help='Número de control del documento (formato 00-000000)'
    )

    # Definimos el tipo de contribuyente de forma independiente
    l10n_ve_taxpayer_type = fields.Selection([
        ('res_re', 'Persona Natural Residente'),
        ('res_nr', 'Persona Natural No Residente'),
        ('dom_re', 'Persona Jurídica Domiciliada'),
        ('dom_nr', 'Persona Jurídica No Domiciliada'),
    ], string='Tipo de Contribuyente')
