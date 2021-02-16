from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError


class Product_List(models.Model):
    _inherit = 'sale.report'
    
    liters_per_unit  = fields.Float(string='Liters per unit')


    

class Sale_Report(models.Model):
    _inherit = 'sale.report'

    product_brand_id  = fields.Many2one('common.product.brand.ept',string='Brand', readonly=True)
    liters_per_unit  = fields.Float('product.template',string='Liters per unit',readonly=True)


    


    
