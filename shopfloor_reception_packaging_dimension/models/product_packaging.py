# Copyright 2025 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import models


class ProductPackaging(models.Model):
    _inherit = "product.packaging"

    def _shopfloor_need_dimension_collection(self):
        return (
            (
                not self.packaging_length
                and self.packaging_level_id.shopfloor_collect_length
            )
            or (not self.width and self.packaging_level_id.shopfloor_collect_width)
            or (not self.height and self.packaging_level_id.shopfloor_collect_height)
            or (not self.weight and self.packaging_level_id.shopfloor_collect_weight)
        )
