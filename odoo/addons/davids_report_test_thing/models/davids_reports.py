from odoo import models, fields, api

class DavidsReport(models.Model):
    _inhert= 'sale.order'
    _name='davidsreports.davidsreports'
    _description= 'davidsreports.davidsreports'

    name = fields.Char()
    rank = fields.Char()
    number = fields.Integer()