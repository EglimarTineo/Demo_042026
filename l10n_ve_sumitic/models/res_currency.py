# -*- coding: utf-8 -*-
from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    @api.model  # <--- CRÍTICO: El Cron necesita que el método sea de modelo
    def _update_ve_bcv_rates(self):
        """ Método para ser llamado por la Acción Planificada """
        # Buscamos la moneda VES (Bolívar)
        currency_ves = self.search([('name', '=', 'VES')], limit=1)
        if not currency_ves:
            _logger.warning("Sumitic: No se encontró la moneda VES en el sistema.")
            return

        # Usando dolarapi.com (muy buena elección para Odoo en Venezuela)
        url = "https://ve.dolarapi.com/v1/dolares/oficial" 
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                # El campo en dolarapi para el oficial es 'promedio' o 'price'
                rate_val = data.get('promedio')
                
                if rate_val and rate_val > 0:
                    # Determinamos la tasa según la moneda base de la compañía
                    company_currency = self.env.company.currency_id
                    
                    # Odoo guarda la tasa como: ¿Cuántas unidades de ESTA moneda equivalen a 1 unidad de la moneda base?
                    # Si la base es USD: 1 USD = 36.50 VES -> rate = 36.50
                    # Si la base es VES: 1 VES = 0.027 USD -> rate = 1/36.50
                    # IMPORTANTE: En Venezuela casi siempre la base es USD o el sistema usa tasa inversa.
                    
                    final_rate = rate_val
                    if company_currency.name == 'VES':
                        final_rate = 1.0 / rate_val

                    # Evitar duplicados para el mismo día
                    existing_rate = self.env['res.currency.rate'].search([
                        ('currency_id', '=', currency_ves.id),
                        ('name', '=', fields.Date.today()),
                        ('company_id', '=', self.env.company.id)
                    ], limit=1)

                    if existing_rate:
                        existing_rate.write({'rate': final_rate})
                        _logger.info("Sumitic: Tasa BCV actualizada (existente): %s", rate_val)
                    else:
                        self.env['res.currency.rate'].create({
                            'currency_id': currency_ves.id,
                            'rate': final_rate,
                            'name': fields.Date.today(),
                            'company_id': self.env.company.id,
                        })
                        _logger.info("Sumitic: Nueva tasa BCV creada: %s", rate_val)
                else:
                    _logger.error("Sumitic: La API no devolvió un valor de tasa válido.")
            else:
                _logger.error("Sumitic: Error de conexión con DolarAPI. Status: %s", response.status_code)
        except Exception as e:
            _logger.error("Sumitic: Error al sincronizar tasa BCV: %s", str(e))
