{
    'name' : 'Decimal',
    'version': '5.2',
    'Summary': 'Change decimal places',
    'description': 'To print the new report',
    'license': 'LGPL-3',
    'depends': [
        'account_accountant',
        'account',
        'account_consolidation',
        'stock',
        'mrp',
        'sale_management',
        'product',
    ],    
     'data': [
        #'views/mrp_view.xml',
        'views/sales_report_view.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':True
}
