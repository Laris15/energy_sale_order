# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class EnergySaleOrder(models.Model):
    _name = 'energy.sale.order'
    _description = 'energy.sale.order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    partner_id = fields.Many2one('res.partner', string="Client", required=True)
    product_template_id = fields.Many2one('product.template', string="Service Type", required=True)
    date_order = fields.Datetime(string="Quotation date", required=True)
    line_ids = fields.One2many('energy.sale.order.line', 'energy_sale_id', string="Energy sale order line", required=True)

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('energy.sale.order') or _('New')

        result = super(EnergySaleOrder, self).create(vals)
        return result


