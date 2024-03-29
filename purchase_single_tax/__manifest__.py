#!/usr/bin/env python3
# -*- coding: utf-8 -*-
{
    'name': "Single Tax for P/O 採購訂單單一稅率",
    'summary': 'One single tax rate for purchase orders. 採購訂單單一稅率.',
    'description': """
Single Tax for P/O 採購訂單單一稅率
================================
**One single tax rate for purchase orders. 採購訂單單一稅率**

*By RichSoda Co., Ltd., Odoo Taiwan. <service@richsoda.com> https://richsoda.com*

This is a module for a web-based opensource business suite, [Odoo](http://odoo.com/).

A tax field in P/O instead of one tax rate per line. Makes all the lines in a P/O the same tax rate.

採購訂單以單一稅率欄位取代每行細項皆有稅率。使所有的訂單細項使用同一稅率。

Features
--------
* Support Odoo v15
* Purchase
    - One single tax rate for P/Os

Contact
-------
If you have any question or advice, please email us at service@richsoda.com or visit our website, https://richsoda.com
    """,
    'author': "RichSoda," "Odoo Taiwan",
    'maintainer': 'RichSoda <service@richsoda.com>',
    'website': "https://www.facebook.com/groups/odoo.taiwan",
    'category': 'Accounting',
    'version': '15.0.1.1',
    'license': 'AGPL-3',
    'depends': [
        'purchase',
        'account',
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "qweb": [
    ],
    'data': [
        'views/purchase_views.xml',
    ],
    'demo': [
    ],
    'images': ['static/description/banner.png'],
    'application': False,
    'auto_install': False,
    'installable': True,
}
