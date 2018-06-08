# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Usuario(models.Model):
    _name = 'intereses.usuario'

    name = fields.Char(string="Nombre")
    foto_usuario = fields.Binary(string="Foto del Usuario")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    pais_id = fields.Many2one('res.country', string="País")
    aficion_id = fields.Many2one('intereses.aficion', string="Aficiones")

class Aficion(models.Model):
    _name = 'intereses.aficion'

    name = fields.Char(string="Afición")
    foto_aficion = fields.Binary(string="Foto")
    aficionados = fields.Integer(string="Número de aficionados")
    usuario_id = fields.One2many('intereses.usuario', 'aficion_id', string="Usuario")