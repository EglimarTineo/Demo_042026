# -*- coding: utf-8 -*-
{
    'name': 'Localización Venezolana Sumitic 360',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Localizations',
    'summary': 'Adaptación de Odoo 19 para la normativa fiscal venezolana (SENIAT)',
    'description': """
        Solución integral Sumitic 360 para Venezuela:
        - Plan de cuentas adaptado.
        - Gestión de impuestos (IVA 16%, 8%, 0%).
        - Estructura territorial completa (Estados, Municipios, Parroquias).
        - Integración con facturación técnica.
    """,
    'author': 'Sumitic 2205 C.A.',
    'website': 'https://sumitic.lat',
    'license': 'LGPL-3',
    
    # ORDEN DE INSTALACIÓN CRÍTICO:
    # Estos módulos se instalan AUTOMÁTICAMENTE antes que el tuyo
    'depends': [
        'base',
        'account',               # Módulo base de Facturación
        'account_accountant',    # Módulo de Contabilidad Completa (Enterprise)
        'account_asset',         # Necesario para el campo 'create_asset'
        'base_vat',              # Validación de RIF/Tax ID
        'l10n_latam_base',       # Base para localizaciones de Latinoamérica
        'l10n_latam_invoice_document', # Manejo de tipos de documentos fiscales
    ],
    
    'data': [
        # 1. Seguridad
        'security/ir.model.access.csv',
        
        # 2. Datos Geográficos (Jerarquía territorial)
        'data/res_country_state_data.xml',
        'data/l10n_ve_hierarchy_data.xml',
        
        # 3. Configuración Contable (Grupos de impuestos)
        'data/account_tax_group_data.xml',
        
        # 4. Plan de Cuentas (Crea las cuentas antes que los impuestos)
        'data/account_account_data.xml', 
        
        # 5. Configuración Fiscal (Impuestos vinculados a las cuentas)
        'data/account_tax_data.xml',
        
        # 6. Procesos Automáticos
        'data/ir_cron_data.xml',
        
        # 7. Vistas de Usuario e Interfaz
        'views/res_partner_views.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/account_move_views.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
