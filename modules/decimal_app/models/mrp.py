from odoo import models, fields, api



class Mrp_production(models.Model):
    _inherit = 'stock.move'
    stock_id = fields.Many2one('stock.quant', string='Stock Quant Id')
    qty_on_hand_in_location = fields.Float('Quantity on Hand(Qty)', compute='compute_qty_on_hand')

    @api.depends('stock_id','location_src_id')
    def compute_qty_on_hand(self):
        for id in self:
            id.qty_on_hand_in_location = id.stock_id.quantity