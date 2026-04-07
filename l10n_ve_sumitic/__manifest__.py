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
    ],
    'data': [
        # 1. Seguridad (Permisos para los nuevos modelos)
        'security/ir.model.access.csv',
        
        # 2. Estructura Geográfica (Estados, Municipios y Parroquias)
        'data/res_country_state_data.xml',
        'data/l10n_ve_hierarchy_data.xml',
        
        # 3. Configuración de Grupos de Impuestos
        'data/account_tax_group_data.xml',
        
        # 4. Plan de Cuentas (DEBE IR ANTES QUE LOS IMPUESTOS)
        'data/account_account_data.xml', 
        
        # 5. Impuestos (Dependen de las cuentas anteriores)
        'data/account_tax_data.xml',
        
        # 6. Automatizaciones y Tareas Programadas
        'data/ir_cron_data.xml',
        
        # 7. Vistas e Interfaz de Usuario
        'views/res_partner_views.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
