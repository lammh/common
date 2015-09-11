# -*- coding: utf-8 -*-
#
#    Author: Kitti Upariphutthiphong
#    Copyright 2014-2015 Ecosoft Co., Ltd.
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
#
{
    'name': "Billing Process",
    'summary': "Group invoice as billing before payment",
    'author': "Ecosoft,Odoo Community Association (OCA)",
    'website': "http://ecosoft.co.th",
    'category': 'Account',
    'version': '0.1.0',
    'depends': ['account',
                'account_voucher',
                'account_accountant',
                # 'account_check_writing'
                ],
    'data': [
        'data/account_billing_data.xml',
        'data/account_billing_sequence.xml',
        'data/account_billing_workflow.xml',
        'security/ir.model.access.csv',
        'views/account_billing.xml',
        'views/voucher_payment_receipt_view.xml',
        # 'demo/account_invoice_demo.xml',
    ],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
