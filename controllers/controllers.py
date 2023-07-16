# -*- coding: utf-8 -*-
# from odoo import http


# class EnergySaleOrder(http.Controller):
#     @http.route('/energy_sale_order/energy_sale_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/energy_sale_order/energy_sale_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('energy_sale_order.listing', {
#             'root': '/energy_sale_order/energy_sale_order',
#             'objects': http.request.env['energy_sale_order.energy_sale_order'].search([]),
#         })

#     @http.route('/energy_sale_order/energy_sale_order/objects/<model("energy_sale_order.energy_sale_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('energy_sale_order.object', {
#             'object': obj
#         })
