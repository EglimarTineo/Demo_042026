# -*- coding: utf-8 -*-
{
    'name': 'Localización Venezolana Sumitic 360',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Localizations',
    'summary': 'Adaptación de Odoo 19 para la normativa fiscal venezolana (SENIAT)',
    'author': 'Sumitic 2205 C.A.',
    'website': 'https://sumitic.lat',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'account',
        'base_vat',
        'l10n_latam_base',
        'l10n_latam_invoice_document',
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_data.xml',
        'data/l10n_ve_hierarchy_data.xml',
        'data/account_tax_group_data.xml',
        
        # 1. Cargamos las cuentas contables primero
        'data/account_account_data.xml', 
        
        # 2. Luego cargamos los impuestos (que usan esas cuentas)
        'data/account_tax_data.xml',
        
        'data/ir_cron_data.xml',
        'views/res_partner_views.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
