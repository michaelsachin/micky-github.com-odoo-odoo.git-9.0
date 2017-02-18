from openerp import models, fields, api, _

class unique_reference(models.Model):
    _inherit = "product.template"
    artnumber = fields.Char(related='default_code', readonly=True, store=True, indexed=True)
    _sql_constraints = [
      ('uniq_artnumber', 'unique(artnumber)', "Alert! This Internal Reference already exists. Please choose a Unique Code. Thankyou!"),
    ]
unique_reference()

