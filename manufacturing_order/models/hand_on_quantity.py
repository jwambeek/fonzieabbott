from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round



class Transfers(models.Model):
    _inherit = 'stock.picking'

    def action_assign(self):
        """ Check availability of picking moves.
        This has the effect of changing the state and reserve quants on available moves, and may
        also impact the state of the picking as it is computed based on move's states.
        @return: True
        """
        #self.filtered(lambda picking: picking.state == 'draft').action_confirm()
        """
        moves = self.mapped('move_lines').filtered(lambda move: move.state not in ('draft', 'cancel', 'done'))
        if not moves:
            raise UserError(_('Nothing to check the availability for.'))
        # If a package level is done when confirmed its location can be different than where it will be reserved.
        # So we remove the move lines created when confirmed to set quantity done to the new reserved ones.
        package_level_done = self.mapped('package_level_ids').filtered(lambda pl: pl.is_done and pl.state == 'confirmed')
        package_level_done.write({'is_done': False})
        moves._action_assign()
        package_level_done.write({'is_done': True})

        return True
        """



"""
class StockQuant(models.Model):
    
    _inherit = 'stock.move'

    inventory_quantity = fields.Float(string='On Hand Quantity', compute='_compute_inventory_quantity' , inverse='_set_inventory_quantity')

    quantity = fields.Float('Quantity', help='Quantity of products in this quant, in the default unit of measure of the product', readonly=True)
    


    @api.depends('quantity')
    def _compute_inventory_quantity(self):
        for quant in self:
            quant.inventory_quantity = quant.quantity

    
    def _get_inventory_move_values():
        print("t")
    
    def _set_inventory_quantity(self):
        for quant in self:
            # Get the quantity to create a move for.
            rounding = quant.product_id.uom_id.rounding
            diff = float_round(quant.inventory_quantity - quant.quantity, precision_rounding=rounding)
            diff_float_compared = float_compare(diff, 0, precision_rounding=rounding)
            # Create and vaidate a move so that the quant matches its `inventory_quantity`.
            if diff_float_compared == 0:
                continue
            elif diff_float_compared > 0:
                move_vals = quant._get_inventory_move_values(diff, quant.product_id.with_company(quant.company_id).property_stock_inventory, quant.location_id)
            else:
                move_vals = quant._get_inventory_move_values(-diff, quant.location_id, quant.product_id.with_company(quant.company_id).property_stock_inventory, out=True)
            move = quant.env['stock.move'].with_context(inventory_mode=False).create(move_vals)
            move._action_done()
"""

