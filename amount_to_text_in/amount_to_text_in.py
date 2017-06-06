# -*- coding: utf-8 -*-
##############################################################################
#MICARC Supply Chain Automation
#
##############################################################################

from openerp import api
from openerp import models, fields
from openerp.tools import amount_to_text_en

class account_invoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def amount_to_text_in(self, amount, currency):
        convert_amount_in_words2 = amount_to_text_en.amount_to_text(amount, lang='en', currency='')
        convert_change_in_words = convert_amount_in_words2.split(' and')[1]
        convert_change_in_words2 = convert_change_in_words.split(' Cent')[0]+' Paise, Only'
        convert_amount_in_words2 = convert_amount_in_words2.split(' and ')[0]+' Rupees and '+convert_change_in_words2
        return convert_amount_in_words2


