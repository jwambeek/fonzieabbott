from odoo import api, fields, models

class StockQuant(models.Model):
    
    _inherit = 'stock.move'

    inventory_quantity = fields.Float(string='On Hand Quantity', compute='_compute_inventory_quantity')

    quantity = fields.Float('Quantity', help='Quantity of products in this quant, in the default unit of measure of the product', readonly=True)
    


    @api.depends('quantity')
    def _compute_inventory_quantity(self):
        for quant in self:
            quant.inventory_quantity = quant.quantity
