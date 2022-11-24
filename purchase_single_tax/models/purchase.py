#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
purchase.py

Modified taxes to single tax
"""

from odoo import models, fields, api, _, exceptions


class PurchaseOrder(models.Model):
    """
    Model of modified the purchase taxes become single tax

    [purchase.order]
    """

    _inherit = 'purchase.order'

    def _get_default_tax(self):
        """
        Get purchase default tax from res.config model

        :return: Purchase default tax
        :rtype: object
        """

        return self.env['ir.values'].get_default('product.template', 'supplier_taxes_id', company_id=self.env.user.company_id.id)

    single_tax = fields.Many2many('account.tax', string='Tax', domain='[("type_tax_use", "=", "purchase")]', default=lambda self: self._get_default_tax())


class PurchaseOrderLine(models.Model):
    """
    Add related to taxes_id filed

    [purchase.order]
    """

    _inherit = 'purchase.order.line'

    taxes_id = fields.Many2many(related='order_id.single_tax')
