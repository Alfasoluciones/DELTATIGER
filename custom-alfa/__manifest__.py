# -*- coding: utf-8 -*-
{
    'name': 'Personalización Alfa',
    'version': '1.00',
    'category': 'Account',
    'sequence': 1,
    'author': 's10 Software',
    'website': 'http://s10.mx',
    'summary': 'Personaliaciones para Alfa',
    'description': """
Contiene:
========
* CFDI: Ajustar precio unitario en XML a facturas con descuento.
    """,
    'depends': [
        "account",
        "account_edi",
        "l10n_mx_edi",
        "l10n_mx_edi_40",
        ],
    'data': [
         ],
    'js': [
        ],
    'installable': True,
    'application': True,
    'active': False
}
