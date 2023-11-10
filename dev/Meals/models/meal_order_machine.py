from odoo import api, fields, models, _

class MealOrderMachine(models.Model):
    _name = 'meal.order.machine'
    _description = 'Meal Order Machine'

    name = fields.Char(string="Machine Name")
    sensor_id = fields.Char(string="Machine Sensor ID", required=True)
    supplier_code = fields.Many2one('meal.supplier', string="Supplier Code")
    location_id = fields.Many2one('meal.location', string="Parent Location", required=True)
    sub_location_id = fields.Many2one('meal.sub.location', string="Sub Location", required=True)
    is_reserved = fields.Boolean(string='Is Reserved', default=False)
