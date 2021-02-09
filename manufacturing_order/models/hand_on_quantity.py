from odoo import api, fields, models, _


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