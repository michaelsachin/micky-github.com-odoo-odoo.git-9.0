# _*_ coding: utf-8 _*_
from openerp import models, fields, api, _
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class z(models.Model):
    _inherit = "sale.order.line"
    x_name = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    x_name1 = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    compname = fields.Char(string='Component Name :', default='NA', compute='_compute_name', store=True)
    x_name2 = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    compmodel = fields.Char(string='Component Model :', defaut='NA', compute='_compute_name', store=True)
    x_name4 = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    custdraw = fields.Char(string='Customer Drawing :', default='NA', compute='_compute_name', store=True)
    x_name6 = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    compdia = fields.Char(string='Component Dia :', defaut='NA', compute='_compute_name', store=True)
    x_name8 = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    compdim = fields.Char(string='Component Dimension :', default='NA', compute='_compute_name', store=True)
    x_name10 = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    x_name11 = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    customdesc = fields.Char(string='Custom Description :', default='NA', compute='_compute_name', store=True)
    x_name13 = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    x_name14 = fields.Char(string='Calculation Field', default='NA', compute='_compute_name', store=True)
    custoper = fields.Char(string='Customer Operation :', default='NA', compute='_compute_name', store=True)
    x_product = fields.Char(related='product_id.name', readonly=True, store=True)

    @api.one
    @api.depends('x_name','x_name1','name','x_name2','compmodel','x_name4','custdraw','x_name6','compdia','x_name8','compdim','x_name10','x_name11','customdesc','x_name13','x_product','x_additional_desc','x_name14','custoper')
    def _compute_name(self):

        if self.product_id and self.name:
            self.x_name = '%s' % sorted(self.name.split(' for'))
            if  "Component Name" in self.x_name:
                self.x_name1 = 'NA'
                self.x_name1 = self.x_name.split('Component Name :')[1]
                self.compname = ' for '+self.x_name1.replace("\\n", "', u").split("', u")[0]
            else:
                self.compname = 'NA'
            if "Component Model Name" in self.x_name:
                self.x_name2 = 'NA'
                self.x_name2 = self.x_name.split('Component Model Name :')[1]
                self.compmodel = ' for model '+self.x_name2.replace("\\n", "', u").split("', u")[0]
            else:
                self.compmodel = 'NA'
            if "Customer Drawing No" in self.x_name:
                self.x_name4 = 'NA'
                self.x_name4 = self.x_name.split('Customer Drawing No :')[1]
                self.custdraw = ' for your drawing no :'+self.x_name4.replace("\\n", "', u").split("', u")[0]
            else:
                self.custdraw = 'NA'
            if "Working Diameter" in self.x_name:
                self.x_name6 = 'NA'
                self.x_name6 = self.x_name.split('Working Diameter :')[1]
                self.compdia = ' for dia :'+self.x_name6.replace("\\n", "', u").split("', u")[0]
            else:
                self.compdia = 'NA'
            if "Operation :" in self.x_name:
                self.x_name14 = 'NA'
                self.x_name14 = self.x_name.split('Operation :')[1]
                self.custoper = ' for Operation :'+self.x_name14.replace("\\n", "', u").split("', u")[0]
            else:
                self.custoper = 'NA'
            if "Dimensional Specification :" in self.x_name:
                self.x_name8 = 'NA'
                self.x_name8 = self.x_name.split('Dimensional Specification :')[1]
                self.compdim = ' and Dimension :'+self.x_name8.replace("\\n", "', u").split("', u")[0]
            else:
                self.compdim = 'NA'
            if "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product
            elif "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname
            elif "NA" in self.compname and "NA" and "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" and "NA" in self.compdim and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdia
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdia and "NA" and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdim
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.compdim and "NA" and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.custdraw
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.custoper
            elif "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel
            elif "NA" in self.compmodel and "NA" in self.compdim and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdia
            elif "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdim
            elif "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.custdraw
            elif "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.custoper
            elif "NA" in self.compname and "NA" in self.compdim and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.compdia
            elif "NA" in self.compname and "NA" in self.compdia and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.compdim
            elif "NA" in self.compname and "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.custdraw
            elif "NA" in self.compname and "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.custoper
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdia+self.compdim
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdim and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdia+self.custdraw
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdim and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdia+self.custdraw
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdim and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdia+self.custoper
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdim+self.custdraw
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdim+self.custoper
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.compdim:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.custdraw+self.custoper
            elif "NA" in self.compdim and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdia
            elif "NA" in self.compdia and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdim
            elif "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.custdraw
            elif "NA" in self.compdia and "NA" in self.compdim and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.custoper
            elif "NA" in self.compdim and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdia
            elif "NA" in self.compmodel and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdia+self.compdim
            elif "NA" in self.compmodel and "NA" in self.compdim and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdia+self.custdraw
            elif "NA" in self.compmodel and "NA" in self.compdim and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdia+self.custoper
            elif "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdim+self.custdraw
            elif "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdim+self.custoper
            elif "NA" in self.compmodel and "NA" in self.compdia and "NA" in self.compdim:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.custdraw+self.custoper
            elif "NA" in self.compname and "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.compdia+self.compdim
            elif "NA" in self.compname and "NA" in self.compdim and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.compdia+self.custdraw
            elif "NA" in self.compname and "NA" in self.compdim and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.compdia+self.custoper
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdia+self.compdim+self.custdraw
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdia+self.compdim+self.custoper
            elif "NA" in self.compname and "NA" in self.compmodel and "NA" in self.compdia:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdim+self.custdraw+self.custoper
            elif "NA" in self.custdraw and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdia+self.compdim
            elif "NA" in self.compdim and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdia+self.custdraw
            elif "NA" in self.compdim and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdia+self.custoper
            elif "NA" in self.compdia and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdim+self.custdraw
            elif "NA" in self.compdia and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdim+self.custoper
            elif "NA" in self.compmodel and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdia+self.compdim+self.custdraw
            elif "NA" in self.compmodel and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdia+self.compdim+self.custoper
            elif "NA" in self.compmodel and "NA" in self.compdim:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdia+self.custdraw+self.custoper
            elif "NA" in self.compmodel and "NA" in self.compdia:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdim+self.custdraw+self.custoper
            elif "NA" in self.compname and "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.compdia+self.compdim+self.custdraw
            elif "NA" in self.compname and "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.compdia+self.compdim+self.custoper
            elif "NA" in self.compname and "NA" in self.compdim:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.compdia+self.custdraw+self.custoper
            elif "NA" in self.compname and "NA" in self.compmodel:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compdia+self.compdim+self.custdraw+self.custoper
            elif "NA" in self.custoper:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdia+self.compdim+self.custdraw
            elif "NA" in self.custdraw:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdia+self.compdim+self.custoper
            elif "NA" in self.compdim:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdia+self.custdraw+self.custoper
            elif "NA" in self.compmodel:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compdia+self.compdim+self.custdraw+self.custoper
            elif "NA" in self.compname:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compmodel+self.compdia+self.compdim+self.custdraw+self.custoper
            else:
                self.x_name13 = 'NA'
                self.x_name13 = '%s' % self.x_product+self.compname+self.compmodel+self.compdia+self.compdim+self.custdraw+self.custoper

        if self.x_name13:
            self.customdesc = '%s' % self.x_name13
        else:
            self.customdesc = 'Waiting for Description'

z()

