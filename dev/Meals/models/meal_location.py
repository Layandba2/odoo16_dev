from odoo import api, fields, models, _


class MealLocation(models.Model):
    _name = 'meal.location'
    _description = 'Meal Location'

    name = fields.Char(string="Name", required=True)
    location_name = fields.Char(string="Location Code", required=True)
    location_address = fields.Char(string="Address")
    sub_location_ids = fields.One2many("meal.sub.location", 'location_id', string="Sub Location Lines")

class MealSubLocation(models.Model):
    _name = 'meal.sub.location'
    _description = 'Meal Sub Location'

    name = fields.Char(string="Name", required=True)
    sub_location_name = fields.Char(string="Sub location Code", required=True)
    location_id = fields.Many2one('meal.location', string="Location")





