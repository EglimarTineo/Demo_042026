# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Venezuela por defecto para agilizar la carga de la contadora
    country_id = fields.Many2one(
        'res.country', 
        string='País', 
        default=lambda self: self.env.ref('base.ve').id
    )
    
    municipality_id = fields.Many2one('res.country.state.municipality', string='Municipio')
    parish_id = fields.Many2one('res.country.state.parish', string='Parroquia')

# --- Clases de Soporte para la Estructura Territorial ---

class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    municipality_ids = fields.One2many('res.country.state.municipality', 'state_id', string='Municipios')

class ResCountryStateMunicipality(models.Model):
    _name = 'res.country.state.municipality'
    _description = 'Municipios de Venezuela'
    _order = 'name'

    name = fields.Char(string='Municipio', required=True)
    state_id = fields.Many2one('res.country.state', string='Estado', required=True)
    parish_ids = fields.One2many('res.country.state.parish', 'municipality_id', string='Parroquias')

class ResCountryStateParish(models.Model):
    _name = 'res.country.state.parish'
    _description = 'Parroquias de Venezuela'
    _order = 'name'

    name = fields.Char(string='Parroquia', required=True)
    municipality_id = fields.Many2one('res.country.state.municipality', string='Municipio', required=True)
