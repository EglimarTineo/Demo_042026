# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_ve_control_number = fields.Char(
        string='Número de Control', 
        copy=False, 
        help="Número de control del formato impreso (SENIAT)"
    )

    # Tipo de contribuyente del cliente en el momento de la factura
    l10n_ve_taxpayer_type = fields.Selection(
        related='partner_id.taxpayer_type', 
        string="Tipo de Contribuyente (Sujeto)",
        store=True
    )

    _sql_constraints = [
        ('unique_control_number', 'unique(l10n_ve_control_number, company_id, move_type)', 
         'El número de control debe ser único por tipo de documento.')
    ]
