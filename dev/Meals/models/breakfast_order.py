from odoo import api, fields, models, _

class BreakfastOrder(models.Model):
    _name = "breakfast.order"
    _description = "Breakfast Orders"

    order_date = fields.Date(string='Order Date', required=True)
    order_reference = fields.Char(string='Order Reference', required=True)
    order_lines = fields.One2many('breakfast.order.line', 'order_id', string='Order Lines')
    supplier = fields.Many2one('meal.supplier', string='Supplier', required=True)
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    order_status = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('billed', 'Billed'),
        ('canceled', 'Canceled'),
    ], string='Order Status', default='draft', readonly=True, copy=False, track_visibility='always')

    def action_confirm_order(self):
        self.write({'order_status': 'confirmed'})
        return True

    def action_cancel_order(self):
        self.write({'order_status': 'canceled'})
        return True

    @api.depends('order_lines.sub_total')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(order.order_lines.mapped('sub_total'))

    def action_create_bill(self):
        self.write({'order_status': 'billed'})

        # Generate the invoice number
        invoice_number = self.env['ir.sequence'].next_by_code('breakfast.invoice.sequence') or 'New'

        # Create the invoice
        invoice_vals = {
            'supplier': self.supplier.id,
            'order_id': self.id,
            'invoice_number': invoice_number,  # Set the generated invoice number
            'total_amount': self.total_amount,
        }
        invoice = self.env['breakfast.invoice'].create(invoice_vals)

        # Create invoice lines based on order lines
        invoice_line_vals = []
        for order_line in self.order_lines:
            invoice_line_vals.append((0, 0, {
                'product': order_line.product.id,
                'quantity': order_line.quantity,
                'unit_price': order_line.unit_price,
            }))
        invoice.write({'order_lines': invoice_line_vals})

        return True

    def action_view_invoice(self):
        self.ensure_one()
        invoice = self.env['breakfast.invoice'].search([('order_id', '=', self.id)], limit=1)
        action = self.env["ir.actions.act_window"].for_xml_id("breakfast.invoice", "action_view_meal_invoice_form")
        action['res_id'] = invoice.id
        return action


class BreakfastOrderLine(models.Model):
    _name = 'breakfast.order.line'
    _description = 'Breakfast Order Line'

    order_id = fields.Many2one('breakfast.order', string='Breakfast Order')
    product = fields.Many2one('meal.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True, default=1.0)
    unit_of_measure = fields.Many2one('uom.uom', string='Unit of Measure', related='product.unit_of_measure',
                                      store=True)
    unit_price = fields.Float(string='Unit Price', related='product.unit_price', store=True)
    sub_total = fields.Float(string='Sub Total', compute='_compute_sub_total', store=True)

    @api.depends('quantity', 'unit_price')
    def _compute_sub_total(self):
        for line in self:
            line.sub_total = line.quantity * line.unit_price

