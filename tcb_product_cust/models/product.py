from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    division = fields.Char(string="Division")
    brand = fields.Char(string="Brand")
    country_of_origin = fields.Char(string="Country of Origin")
    region = fields.Char(string="Region")
    