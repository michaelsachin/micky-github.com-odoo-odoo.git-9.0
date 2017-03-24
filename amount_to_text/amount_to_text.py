# -*- coding: utf-8 -*-
##############################################################################
#    
#
##############################################################################

from openerp import api
from openerp import models, fields
from openerp.tools import amount_to_text_en

class account_invoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def amount_to_text(self, amount, currency):
        convert_amount_in_words = amount_to_text_en.amount_to_text(amount, lang='en', currency='')
        convert_amount_in_words = convert_amount_in_words.split(' and')[0]+' Only'
        return convert_amount_in_words


