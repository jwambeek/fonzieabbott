from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError
from odoo.tools import float_compare, float_round, float_is_zero, format_datetime
from odoo.tools.misc import format_date

from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES

SIZE_BACK_ORDER_NUMERING = 3


class Mrp_Production(models.Model):
    
    _inherit = 'mrp.production'

    
    stock_on_quantity = fields.Float(
        'Stock on Quantity',
        help='Quantity of products in this quant, in the default unit of measure of the product',
        readonly=True)
    

    """
    @api.depends('quantity')
    def _compute_inventory_quantity(self):
        if not self._is_inventory_mode():
            self.inventory_quantity = 0
            return
        for quant in self:
            quant.inventory_quantity = quant.quantity

    """