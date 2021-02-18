# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Manufacturing',
    'version': '2.3',
    
    'category': 'Manufacturing/Manufacturing',
    'sequence': 55,
    'summary': 'Manufacturing Orders & BOMs',
    'depends': [
        'account_accountant',
        'account',
        'account_consolidation',
        'stock',
        'mrp',
        'sale_management',
        'product',
    ],
    'description': "",
   # 'data': [
        #'security/mrp_security.xml',
        #'security/ir.model.access.csv',
        #'views/hand_on_quantity.xml',
 #   ],
   
    
    'application': True,
    'installable': True,
    'auto_install':True
}
