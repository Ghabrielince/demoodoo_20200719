# -*- coding: utf-8 -*-

from odoo import models, fields


class MascotasMascotas(models.Model):
    _name = "mascotas.mascotas"

    # Lista de campos de la tabla.
    name = fields.Char(string="Nombre")
    tipo_id = fields.Many2one("mascotas.tipos", string="Tipo")
    raza_id = fields.Many2one("mascotas.razas", string="Raza")
    fecha_nacimiento = fields.Date(string="Fec. Nac.")
    sexo = fields.Selection([("m", "Macho"), ("h", "Hembra")], string="Sexo")

class MascotasRazas(models.Model):
    _name = "mascotas.razas"

    name = fields.Char(string="Nombre")
    codigo = fields.Char(string="Código")

class MascotasTipos(models.Model):
    _name = "mascotas.tipos"

    name = fields.Char(string="Nombre")
    codigo = fields.Char(string="Código")