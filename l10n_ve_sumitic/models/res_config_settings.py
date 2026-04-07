# -*- coding: utf-8 -*-
from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # Relacionamos los campos de la compañía para que sean editables desde Ajustes
    vat = fields.Char(related='company_id.vat', readonly=False)
    taxpayer_type = fields.Selection(related='company_id.taxpayer_type', readonly=False)
    
    l10n_ve_igtf_tax_id = fields.Many2one(
        'account.tax', 
        string="Impuesto IGTF por Defecto",
        config_parameter='l10n_ve_sumitic.igtf_tax_id'
    )
