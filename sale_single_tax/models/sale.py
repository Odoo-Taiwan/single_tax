#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sale.py

Modified taxes to single tax
"""

from odoo import models, fields, api, _, exceptions


class SaleOrder(models.Model):
    """
    Model of modified the sale taxes become single tax

    [sale.order]
    """

    _inherit = 'sale.order'

    single_tax = fields.Many2many('account.tax', string='Tax', domain='[("type_tax_use", "=", "sale")]', default=lambda self: self.env.user.company_id.account_sale_tax_id)


class SaleOrderLine(models.Model):
    """
    Add related to tax_id filed

    [sale.order.line]
    """

    _inherit = 'sale.order.line'

    tax_id = fields.Many2many(related='order_id.single_tax')
