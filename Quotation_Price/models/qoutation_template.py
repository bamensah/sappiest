# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import api, fields, models

class ProductPricing(models.Model):
    _name = 'qoutation.price'
    _inherits = {'sale.order':'price_unit'}

class QoutationPrice(models.Model):
_inherit = 'qoutation.price'
    unit_price = fields.Float(string='Unit Price')
