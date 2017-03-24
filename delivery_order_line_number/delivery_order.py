from openerp import models, api, fields


class delivery_order_line(models.Model):

    _inherit = 'stock.pack.operation'

    number = fields.Integer(compute='get_number', store=True)

    @api.multi
    @api.depends('picking_id')
    def get_number(self):
        for order in self.mapped('picking_id'):
            number = 1
            for line in order.pack_operation_ids:
                line.number = number
                number += 1
