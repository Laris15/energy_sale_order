# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EnergySaleOrder(models.Model):
    _name = 'energy.sale.order.line'
    _description = 'energy.sale.order.line'

    energy_sale_id = fields.Many2one('energy.sale.order')
    address = fields.Char(string="Address", required=True)
    location = fields.Char(string="Location", required=True)
    quantity = fields.Float(string="Quantity", required=True)


