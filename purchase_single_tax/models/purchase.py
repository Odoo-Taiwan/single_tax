#!/usr/bin/env python3
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

    single_tax = fields.Many2one('account.tax', string='Tax', domain='[("type_tax_use", "=", "purchase")]', default=lambda self: self.env.user.company_id.account_purchase_tax_id)


class PurchaseOrderLine(models.Model):
    """
    Add related to taxes_id filed

    [purchase.order]
    """

    _inherit = 'purchase.order.line'

    taxes_id = fields.Many2many(related='order_id.single_tax')
