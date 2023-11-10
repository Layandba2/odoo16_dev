from odoo import api, fields, models, _


class MealSupplier(models.Model):
    _name = 'meal.supplier'
    _description = 'Meal Supplier'




    #supplier_name = fields.Char(string="Supplier Code", required=True)
    name = fields.Char(string="Name", required=True)
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    city = fields.Char(string="City")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    machine_id = fields.Many2one('meal.order.machine', string='Supplier Machine Code')
    is_active = fields.Boolean(string="Is Active", required=True)


