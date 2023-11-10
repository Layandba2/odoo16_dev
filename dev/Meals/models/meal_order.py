
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from datetime import datetime
import xlrd
import tempfile
import binascii



class MealOrder(models.Model):
    _name = 'meal.order'
    _description = 'Meal Order'

    employee_id = fields.Char(string="Employee")
    order_date_time = fields.Date(string="Check In")
    supplier_id = fields.Many2one('meal.supplier',string="Supplier")
    location_id = fields.Many2one('meal.location', string="Location")
    sub_location_id = fields.Many2one('meal.sub.location', string="Sub Location")

    def button_import_xlsx_contacts(self):
        workbook = xlrd.open_workbook('E:\\Odoo\\odoo-16.0\\dev\\Meals\\models\\data.xlsx', on_demand=True)
        sheet = workbook.sheet_by_index(0)

        if sheet.ncols == 0:
            return

        first_row = []
        for col in range(sheet.ncols):
            first_row.append(sheet.cell_value(0, col))

        import_lines = []
        for row in range(1, sheet.nrows):
            line = {}
            for col in range(sheet.ncols):
                line[first_row[col]] = sheet.cell_value(row, col)
            import_lines.append(line)
        date_format = '%m/%d/%Y %I:%M %p'
        partner_ids = []
        for import_line in import_lines:
            partner_ids.append(self.env['meal.order'].create({
                'employee_id': str(import_line.get('employee_id')).replace(".0",""),
                'order_date_time': datetime.strptime(import_line.get('order_date_time'),date_format),
                'supplier_id': str(import_line.get('supplier_id')).replace(".0",""),
            }).id)


