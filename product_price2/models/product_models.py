# -*- coding: utf-8 -*-

from odoo import models, fields

class PrpductTemplateHerencia(models.Model):
    _inherit = "product.template"

    price_2 = fields.Monetary("Precio 2")