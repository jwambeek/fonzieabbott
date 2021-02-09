from odoo import api, fields, models

class StockQuant(models.Model):
    
    _inherit = 'stock.move'

    inventory_quantity = fields.Float(string='Hand On quantity', compute='_compute_inventory_quantity')

    quantity = fields.Float(
        'Quantity',
        help='Quantity of products in this quant, in the default unit of measure of the product',
        readonly=True)
    


    @api.depends('quantity')
    def _compute_inventory_quantity(self):
        if not self._is_inventory_mode():
            self.inventory_quantity = 0
            return
        for quant in self:
            quant.inventory_quantity = quant.quantity
