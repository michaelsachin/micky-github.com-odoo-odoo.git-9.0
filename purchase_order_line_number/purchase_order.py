from openerp import models, api, fields


class purchase_order_line(models.Model):

    _inherit = 'purchase.order.line'

    number = fields.Integer(compute='get_number', store=True)

    @api.multi
    @api.depends('order_id')
    def get_number(self):
        for order in self.mapped('order_id'):
            number = 1
            for line in order.order_line:
                line.number = number
                number += 1
