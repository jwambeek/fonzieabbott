{
    'name' : 'Deciaml',
    'version': '1.3',
    'Summary': 'Change decimal places',
    'description': 'To print the new report',
    'license': 'LGPL-3',
    'depends': [
        'account_accountant',
        'account',
        'account_consolidation',
        'stock',
        'mrp',
    ],    
    'data': [
        'views/mrp_view.xml',
    ],
    'installable': True,
    'application':True,
    'auto_install':True
}