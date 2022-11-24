#!/usr/bin/env python
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

    def _get_default_tax(self):
        """
        Get sale default tax from res.config model

        :return: Default tax record
        :rtype: object
        """

        return self.env['ir.values'].get_default('product.template', 'taxes_id', company_id=self.env.user.company_id.id)

    single_tax = fields.Many2many('account.tax', string='Tax', domain='[("type_tax_use", "=", "sale")]', default=lambda self: self._get_default_tax())


class SaleOrderLine(models.Model):
    """
    Add related to tax_id filed

    [sale.order.line]
    """

    _inherit = 'sale.order.line'

    tax_id = fields.Many2many(related='order_id.single_tax')
