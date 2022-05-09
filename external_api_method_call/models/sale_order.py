# -*- coding: utf-8 -*-

from odoo import models, api, fields, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def example_method(self, test):
        return test