from odoo import models, fields, api


class Decimal_app(models.Model):
    _inherit= 'account.asset'
    method_progress_factor = fields.Float(string='Declining Factor', digits=(12, 4))

