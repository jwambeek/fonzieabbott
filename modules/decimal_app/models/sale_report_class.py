from odoo import models, fields, api
from odoo import tools

class Sale_Product(models.Model):
    _inherit = 'product.template'

    alcohol_perc = fields.Float(string='Alcohol%%')
