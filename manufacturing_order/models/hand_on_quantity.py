from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError
from odoo.tools import float_compare, float_round, float_is_zero, format_datetime
from odoo.tools.misc import format_date

from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES

SIZE_BACK_ORDER_NUMERING = 3


class MrpProduction(models.Model):
    
    _inherit = 'mrp.production'

    inventory_quantity = fields.Float(
        'Inventoried Quantity', compute='_compute_inventory_quantity',
        inverse='_set_inventory_quantity', groups='stock.group_stock_manager')

    quantity = fields.Float(
        'Quantity',
        help='Quantity of products in this quant, in the default unit of measure of the product',
        readonly=True)
    

  
  
           
