from odoo import api, fields, models, _


class BreakfastInvoice(models.Model):

    _name = "breakfast.invoice"
    _description = "Breakfast Invoice"

    order_id = fields.Many2one('breakfast.order', string='Order', required=True)
    order_reference = fields.Char(string='Order Reference', related='order_id.order_reference', readonly=True)
    supplier = fields.Many2one('meal.supplier', string='Supplier', required=True)
    order_lines = fields.One2many('meal.invoice.line', 'invoice_id', string='Order Lines')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    invoice_number = fields.Char(string='Invoice Number', required=True, readonly=True, copy=False, default='New')
    order_date = fields.Date(string="Order Date", related='order_id.order_date', readonly=True)
    @api.model
    def create(self, vals):
        if vals.get('invoice_number', 'New') == 'New':
            vals['invoice_number'] = self.env['ir.sequence'].next_by_code('breakfast.invoice.sequence') or 'New'
        return super(BreakfastInvoice, self).create(vals)

    @api.depends('order_lines.sub_total')
    def _compute_total_amount(self):
        for invoice in self:
            invoice.total_amount = sum(invoice.order_lines.mapped('sub_total'))


class MealInvoiceLine(models.Model):
    _name = 'meal.invoice.line'

    invoice_id = fields.Many2one('breakfast.invoice', string='Invoice')
    product = fields.Many2one('meal.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True, default=1.0)
    unit_price = fields.Float(string='Unit Price', required=True)
    sub_total = fields.Float(string='Sub Total', compute='_compute_sub_total', store=True)

    @api.depends('quantity', 'unit_price')
    def _compute_sub_total(self):
        for line in self:
            line.sub_total = line.quantity * line.unit_price

