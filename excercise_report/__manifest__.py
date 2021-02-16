# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Manufacturing',
    'version': '3.5',
    
    'category': 'Manufacturing/Manufacturing',
    'sequence': 55,
    'summary': 'Manufacturing Orders & BOMs',
    'depends': ['product','sale_management' ],
    'description': "",
    'data': [
        #'security/mrp_security.xml',
        #'security/ir.model.access.csv',
        #'views/hand_on_quantity.xml',
        'views/product_list_pivot.xml',
    ],
   
    
    'application': True,
    'installable': True,
    'auto_install':False
}
