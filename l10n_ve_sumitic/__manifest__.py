{
    'name': 'Venezuela - Contabilidad Sumitic',
    'version': '19.0.1.0.0',
    'summary': 'Localización Contable para Venezuela adaptada para Odoo 19',
    'category': 'Accounting/Localizations/Account Charts', # <--- CORREGIDO CON 'S'
    'author': 'Sumitic',
    'website': 'https://sumitic.lat',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'account_accountant', # RECOMENDADO: Para que active el menú de Contabilidad completo
        'base_vat',
        'l10n_ve',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/res_country_state_data.xml',
        'data/account.account.csv',
        'data/account_tax_group_data.xml',
        'data/account_tax_data.xml',
        'data/ir_cron_data.xml',
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/account_move.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
