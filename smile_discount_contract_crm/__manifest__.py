# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 GreenBiz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Discount Contract CRM',
    'version': '0.1',
    'author': 'Smile',
    'category': 'Hidden',
    'description': """
Discount Contract CRM
=====================
""",
    'website': 'http://www.smile.fr',
    'images': [],
    'depends': [
        'col_discount_contract',
        'crm',
    ],
    'data': [
        "views/discount_contract_view.xml",
        "views/crm_lead_view.xml",
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': True,
}
