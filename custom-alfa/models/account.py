# -*- encoding: utf-8 -*-
###########################################################################
#  S10 Software
###########################################################################

from odoo import _, api, fields, models, tools, registry


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def _prepare_edi_vals_to_export(self):
        '''
        ** Override
          Retira los descuentos y cambia el precio unitario
        :return: A python dict containing default pre-processed values.
        '''
        self.ensure_one()
        res = super()._prepare_edi_vals_to_export()

        if self.discount == 100.0:
            gross_price_subtotal = 0
        else:
            gross_price_subtotal = self.currency_id.round(self.price_subtotal)

        price_unit_after_discount = res.get('price_unit_after_discount')
        res.update({
            'price_subtotal_before_discount': gross_price_subtotal,
            'gross_price_total_unit': price_unit_after_discount,
            'price_discount': 0.0,
            'price_discount_unit': 0.0,
        })
        return res

