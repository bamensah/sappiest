# -*- coding: utf-8 -*-

from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property Listing"

    name = fields.Char(required=True)
    description = field.Text()
    postcode = field.Char()
    date_availability = field.Date()
    expected_price = field.Float(required=True)
    selling_price = field.Float()
    bedrooms = field.Integer()
    living_area = field.Integer()
    facades = field.Integer()
    garage = field.Boolean()
    garden = field.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('north', 'North'), ('south','South'), ('east','East'), ('west','West')],
        help="Garden Orientation is used for Garden location"
    )
