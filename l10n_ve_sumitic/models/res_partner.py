# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # 1. País por defecto (Venezuela) para agilizar la carga de datos
    country_id = fields.Many2one(
        'res.country', 
        string='País', 
        default=lambda self: self.env.ref('base.ve', raise_if_not_found=False).id
    )
    
    # 2. Campos territoriales específicos para Venezuela
    municipality_id = fields.Many2one('res.country.state.municipality', string='Municipio')
    parish_id = fields.Many2one('res.country.state.parish', string='Parroquia')

    # 3. CAMPO REQUERIDO POR TU VISTA XML (El que causaba el error de "Field does not exist")
    l10n_ve_responsibility_type_id = fields.Many2one(
        'l10n_ve.responsibility.type', 
        string='Tipo de Responsabilidad'
    )

# --- CLASES DE SOPORTE PARA LA ESTRUCTURA TERRITORIAL ---

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

# --- MODELO PARA RESPONSABILIDAD FISCAL (SENIAT) ---

class L10nVeResponsibilityType(models.Model):
    _name = 'l10n_ve.responsibility.type'
    _description = 'Tipos de Responsabilidad Fiscal VE'
    _order = 'name'

    name = fields.Char(string='Descripción', required=True) # Ejemplo: Contribuyente Especial, Ordinario, etc.
    code = fields.Char(string='Código')
