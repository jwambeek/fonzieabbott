import logging

from psycopg2 import Error, OperationalError

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression
from odoo.tools.float_utils import float_compare, float_is_zero, float_round


#from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES



class StockQuant(models.Model):
    
    _inherit = 'mrp.production'

    inventory_quantity = fields.Float(string="Hand On Quantity")

    
