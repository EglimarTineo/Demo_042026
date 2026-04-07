{
    'name': 'Venezuela - Contabilidad Sumitic',
    'version': '19.0.1.0.0',
    'summary': 'Localización Contable para Venezuela adaptada para Odoo 19 Enterprise',
    'category': 'Accounting/Localizations/Account Charts',
    'author': 'Sumitic',
    'website': 'https://sumitic.lat',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'account',
        'account_accountant',
        'account_asset',
        'base_vat',
        'l10n_ve',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_data.xml',
        'data/l10n_ve_hierarchy_data.xml',
        'data/account_tax_group_data.xml',
        
        # --- CAMBIO CRÍTICO AQUÍ ---
        'data/account_account_data.xml', # 1. Primero creamos las cuentas
        'data/account_tax_data.xml',     # 2. Luego los impuestos que usan esas cuentas
        # ---------------------------
        
        'data/ir_cron_data.xml',
        'views/res_partner_views.xml'
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/account_move.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
