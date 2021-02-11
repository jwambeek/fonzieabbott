from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero, float_round

"""
class Sale_Report(models.Model):
    _inherit = 'sale.report'

    brand  = fields.Float(related='product_id.product_brand_id', readonly=True)
"""

class Transfers(models.Model):
    _inherit = 'stock.picking'

    def action_assign(self):
        """ Check availability of picking moves.
        This has the effect of changing the state and reserve quants on available moves, and may
        also impact the state of the picking as it is computed based on move's states.
        @return: True
        """
        self.filtered(lambda picking: picking.state == 'draft').action_confirm()
        
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
        



