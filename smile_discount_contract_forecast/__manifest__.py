# -*- encoding: utf-8 -*-
##############################################################################
#
#    odoo, Open Source Management Solution
#    Copyright (C) 2017 Smile (<http://www.smile.fr>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Discount Contract Forecast",
    "version": "0.1",
    "depends": [
        "smile_discount_contract",
    ],
    "author": "Smile",
    "license": 'AGPL-3',
    "description": """
Discount Contract Forecast
==========================

Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr
    """,
    "website": "http://www.smile.fr",
    'category': 'Accounting',
    "sequence": 0,
    "data": [
        "security/ir.model.access.csv",
        "views/discount_contract_view.xml",
        "views/discount_contract_line_view.xml",
        "views/discount_contract_forecast_method_view.xml",
        "views/menus.xml",
        "data/discount.contract.forecast_method.csv",
    ],
    "demo": [],
    "auto_install": False,
    "installable": True,
    "application": False,
}
