# -*- coding: utf-8 -*-

from openerp import fields, models, api, _
from datetime import datetime
from openerp.tools.amount_to_text_en import *


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection([
        ('draft', 'Draft PO'),
        ('sent', 'RFQ Sent'),
        ('bid', 'Bid'),
        ('revise', 'Revised'),
        ('purchase', 'Purchase Order'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    revision_no = fields.Integer('Revision Number', default=0, copy=False)
    revised_po_id = fields.Many2one('purchase.order', 'Revised From', copy=False)
    p_rev_order_id = fields.Integer('Rev Order id', copy=False)

    @api.multi
    def revise_purchase_order(self):
        if self.revised_po_id:
            name = self.name.split('-R')[0]+'-R'+str(self.revision_no+1)
            values = {
            'state': 'draft',
            'name': name,
            'revised_po_id': self.id,
            'revision_no': self.revision_no+1,
        }
        else:
            name = self.name+'-'+'R'+str(self.revision_no+1)
            values = {
            'state': 'draft',
            'name': name,
            'revised_po_id': self.id,
            'revision_no': self.revision_no+1,
        }
        p_rev_order_id = self.copy(default=values)
        self.write({'state': 'revise'})
        return {
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'purchase.order',
            'res_id': p_rev_order_id.id,
            'type': 'ir.actions.act_window',
        }

