# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class AccountPaymentGroup(models.Model):
    _inherit = "account.payment.group"

    def name_get(self):
        """
        Override to show first payment name when payment group has no name
        """
        result = []
        for rec in self:
            # If payment group has a name, use it
            if rec.name and rec.name != '/':
                name = rec.name
            # Otherwise, try to get the first payment's name
            elif rec.payment_ids and rec.payment_ids[0].name:
                name = rec.payment_ids[0].name
            # If nothing works, use 'Draft Payment Group' or the ID
            else:
                name = 'Payment Group %s' % rec.id

            result.append((rec.id, name))
        return result
