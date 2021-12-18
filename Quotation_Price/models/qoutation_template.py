# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models

class ProductPricing(models.Model):
    _inherits = 'sale.order.line'
    des_head = fields.Char(string='Unit Price')
