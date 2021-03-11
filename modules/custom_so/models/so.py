from odoo import models, fields, api

class CustomField(models.Model):
    _inherit= 'sale.order'
    custom_payment_method = fields.Char(string='Payment Method')

