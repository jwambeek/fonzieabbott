from odoo import models, fields, api
from odoo import tools

class Sale_Report_Class(models.Model):
    _inherit = 'sale.report'

    liters_sold = fields.Float(string ='Liters per Unit', readonly=True)
    total_liters_sold = fields.Float(string ='Total Liters Sold', readonly=True)


    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        with_ = ("WITH %s" % with_clause) if with_clause else ""

        select_ = """
           t.x_studio_liters_per_unit_eg_03_for_300ml as liters_sold,
            (count(*) * t.x_studio_liters_per_unit_eg_03_for_300ml) as total_liters_sold,
            s.id as order_id
        """

        for field in fields.values():
            select_ += field

        from_ = """
                sale_order_line l
                      right outer join sale_order s on (s.id=l.order_id)
                      join res_partner partner on s.partner_id = partner.id
                        left join product_product p on (l.product_id=p.id)
                            left join product_template t on (p.product_tmpl_id=t.id)
                    left join uom_uom u on (u.id=l.product_uom)
                    left join uom_uom u2 on (u2.id=t.uom_id)
                    left join product_pricelist pp on (s.pricelist_id = pp.id)
                %s
        """ % from_clause

        groupby_ = """
            
            t.x_studio_liters_per_unit_eg_03_for_300ml,
           
            s.id %s
        """ % (groupby)

        return '%s (SELECT %s FROM %s GROUP BY %s)' % (with_, select_, from_, groupby_)
