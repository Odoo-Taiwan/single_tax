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

    single_tax = fields.Many2one('account.tax', string='Tax', domain='[("type_tax_use", "=", "sale")]')

    @api.multi
    @api.onchange('single_tax', 'order_line', 'order_line.product_id', 'order_line.tax_id')
    def single_tax_change(self):
        """
        When those field change will change product taxes in order line field

        :return: None
        """

        for order in self:
            for line in order.order_line:
                line.tax_id = order.single_tax

    def action_confirm(self):
        """
        When user confirm the order. Product tax will become same as single tax

        :return: None
        """

        self.single_tax_change()
        return super(SaleOrder, self).action_confirm()

    def action_quotation_send(self):
        """
        When user send the quotation of order. Product tax will become same as single tax

        :return: Action
        """

        self.single_tax_change()
        return super(SaleOrder, self).action_quotation_send()
