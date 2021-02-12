from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError
#from odoo.tools.float_utils import float_compare, float_is_zero, float_round


class Sale_Report(models.Model):
    _inherit = 'sale.report'

    product_brand_id  = fields.Many2one('common.product.brand.ept',string='Brand', readonly=True)

    


    