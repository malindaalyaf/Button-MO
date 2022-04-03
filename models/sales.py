from odoo import models


class Sales_MO(models.Model):
    _inherit = 'sale.order'

    def mo_button(self):
        mo = []
        mo_auto_target = self.env['sale.order'].browse(self.id)
        # print("a")
        for a in mo_auto_target:
            mo.append([{
                'product_id': a.order_line.product_id.id,
                'product_uom_id': a.order_line.product_id.bom_ids.product_uom_id.id,
                'bom_id': a.order_line.product_id.bom_ids.id,
                'harga_bom': a.order_line.product_id.bom_ids.harga_bom,
                'product_qty': a.order_line.product_uom_qty,
            }])

        proid = mo[0][0]["product_id"]
        pro_uom_id = mo[0][0]["product_uom_id"]
        bomid = mo[0][0]["bom_id"]
        bom_price = mo[0][0]["harga_bom"]
        proqty = mo[0][0]["product_qty"]

        if bom_price:
            self.env['mrp.production'].create(
                {'product_id': proid, "product_uom_id": pro_uom_id, "bom_id": bomid, "product_qty": proqty})
        else:
            pass