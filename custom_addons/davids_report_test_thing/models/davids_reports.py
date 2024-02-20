from odoo import models, fields

class davids_report(models.Model):
    _name='davidsreports.davidsreports'
    _description= 'davidsreports.davidsreports'

    name = fields.Char()
    rank = fields.Char()
    number = fields.Integer()