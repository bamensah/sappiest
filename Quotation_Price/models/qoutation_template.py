# -*- coding: utf-8 -*-
# Copyright (c) iSoft Solutions Limited

from odoo import fields, models

class ProductPricing(models.Model):
    _inherit = "sale.order.template"

    des_head = fields.Char(string='Header')
