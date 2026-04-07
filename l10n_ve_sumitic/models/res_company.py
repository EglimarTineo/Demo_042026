# -*- coding: utf-8 -*-
from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    vat = fields.Char(string="RIF", help="Registro de Información Fiscal")
    
    taxpayer_type = fields.Selection([
        ('formal', 'Formal'),
        ('special', 'Especial'),
        ('ordinary', 'Ordinario'),
    ], string="Tipo de Contribuyente", default='ordinary')

    # Configuración para el comprobante de retención
    retention_iva_sequence_id = fields.Many2one('ir.sequence', string="Secuencia de Retención IVA")
    retention_islr_sequence_id = fields.Many2one('ir.sequence', string="Secuencia de Retención ISLR")
