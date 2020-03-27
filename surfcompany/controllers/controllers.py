# -*- coding: utf-8 -*-
from odoo import http

# class Surfcompany(http.Controller):
#     @http.route('/surfcompany/surfcompany/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/surfcompany/surfcompany/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('surfcompany.listing', {
#             'root': '/surfcompany/surfcompany',
#             'objects': http.request.env['surfcompany.surfcompany'].search([]),
#         })

#     @http.route('/surfcompany/surfcompany/objects/<model("surfcompany.surfcompany"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('surfcompany.object', {
#             'object': obj
#         })