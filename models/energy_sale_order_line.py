# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EnergySaleOrder(models.Model):
    _name = 'energy.sale.order.line'
    _description = 'energy.sale.order.line'

    energy_sale_id = fields.Many2one('energy.sale.order')
    address = fields.Char(string="Address")
    location = fields.Char(string="Location")
    quantity = fields.Float(string="Quantity")


