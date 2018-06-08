# -*- coding: utf-8 -*-
from odoo import http

# class Intereses(http.Controller):
#     @http.route('/intereses/intereses/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/intereses/intereses/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('intereses.listing', {
#             'root': '/intereses/intereses',
#             'objects': http.request.env['intereses.intereses'].search([]),
#         })

#     @http.route('/intereses/intereses/objects/<model("intereses.intereses"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('intereses.object', {
#             'object': obj
#         })