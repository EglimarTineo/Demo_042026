# -*- coding: utf-8 -*-
from odoo import models, fields, api
import requests
import logging

_logger = logging.getLogger(__name__)

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    def _update_ve_bcv_rates(self):
        """ Método para ser llamado por la Acción Planificada """
        # Buscamos la moneda VES
        currency_ves = self.search([('name', '=', 'VES')], limit=1)
        if not currency_ves:
            return

        # URL de un servicio espejo confiable o API de terceros
        # Nota: En producción, Sumitic podría usar su propio microservicio de scraping
        url = "https://ve.dolarapi.com/v1/dolares/oficial" 
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                # El BCV da el precio en Bs/USD (ej: 36.50)
                # Odoo requiere la tasa inversa (1 USD = X Bs) si la moneda base es USD
                # O simplemente el valor si la moneda base es VES.
                rate_val = data.get('promedio')
                
                if rate_val:
                    self.env['res.currency.rate'].create({
                        'currency_id': currency_ves.id,
                        'rate': 1.0 / rate_val if self.env.company.currency_id.name == 'USD' else rate_val,
                        'name': fields.Date.today(),
                        'company_id': self.env.company.id,
                    })
                    _logger.info("Sumitic: Tasa BCV actualizada con éxito: %s", rate_val)
        except Exception as e:
            _logger.error("Sumitic: Error al sincronizar tasa BCV: %s", str(e))
