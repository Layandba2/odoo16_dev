from odoo import api, fields, models, _


class MealRotation(models.Model):
    _name = 'meal.rotation'
    _description = 'Meal Rotation'

    location_id = fields.Many2one('meal.location',string="Location", required=True)
    supplier_id = fields.Many2one('meal.supplier',string="Supplier", required=True)
    rotation_date = fields.Datetime(string="Rotation Date")