from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round



class Sale_Order(models.Model):
    _inherit = 'sale.order'

class Product_Template(models.Model):
    _inherit = 'product.template'


     



