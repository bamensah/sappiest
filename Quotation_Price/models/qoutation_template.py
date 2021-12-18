# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models

class ProductPricing(models.Model):
    _inherit = ['sale.order.template', 'sale.order']
    price_unit = fields.Float('Unit Price')
