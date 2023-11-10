from odoo import api, fields, models, _

class MealProduct(models.Model):
    _name = "meal.product"
    _description = "Meal Product"

    name = fields.Char(string="Product Name", required=True)
    product_code = fields.Char(string="Product Code", required=True)
    unit_of_measure = fields.Many2one('uom.uom', string="Unit Of Measure", required=True)
    unit_price = fields.Float(string="Unit Price", required=True)
