{
    'name': 'Venezuela - Contabilidad Sumitic',
    'version': '19.0.1.0.0',
    'summary': 'Localización Contable para Venezuela adaptada para Odoo 19',
    'category': 'Accounting/Localizations/Account Charts',
    'author': 'Sumitic',
    'website': 'https://sumitic.lat',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'account_accountant', 
        'account_asset',      # <--- AGREGAR ESTO: Evita el error de 'create_asset'
        'base_vat',
        'l10n_ve',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_data.xml',
        # 'data/account_account_data.xml', # Recomendación: Ponerlo después de impuestos si estos se usan en las cuentas
        'data/account_tax_group_data.xml',
        'data/account_tax_data.xml',
        'data/account_account_data.xml', # <--- MOVIDO: Mejor cargar cuentas después de grupos e impuestos
        'data/ir_cron_data.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/account_move.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
