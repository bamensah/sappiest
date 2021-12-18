# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models

class ProductPricing(models.Model):
    _inherit = 'sale.order.template'
    unit_price = fields.Float('Unit Price')
