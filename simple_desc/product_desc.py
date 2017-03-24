from openerp import models, fields, api, _

class y(models.Model):
    _inherit = "product.template"
    simpledesc = fields.Char(string='Simple Description :', compute='_compute_group', store=True)

    @api.depends('default_code','name')
    def _compute_group(self):

        if self.x_testing and self.name:
            self.simpledesc = 'The Internal Reference for'+' '+self.name+' '+'is'+' '+self.default_code
        else:
            self.simpledesc = 'Please Enter Internal Reference to update Description'


