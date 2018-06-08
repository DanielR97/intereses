# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Aficionado(models.Model):
    _name = 'intereses.aficionado'

    name = fields.Char(string="Nombre")
    foto_aficionado = fields.Binary(string="Foto del usuario")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    pais_id = fields.Many2one('res.country', string="País")
    aficion_id = fields.Many2one('intereses.aficion', string="Aficiones")

class Aficion(models.Model):
    _name = 'intereses.aficion'

    name = fields.Char(string="Afición")
    foto_aficion = fields.Binary(string="Foto")
    aficionados = fields.Integer(string="Número de aficionados")
    aficionado_id = fields.One2many('intereses.aficionado', 'aficion_id', string="Aficionado")

class Reunion(models.Model):
    _name = 'intereses.reunion'

    name = fields.Char(string="Motivo de reunión")
    fecha_reunion = fields.Datetime(string="Fecha y hora")
    lugar_reunion = fields.Selection([('londres','Londres'),('barcelona','Barcelona'),('boston','Boston')])
    puntos = fields.Text(string="Puntos a tratar en la reunión")