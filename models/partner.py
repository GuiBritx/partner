
from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_client = fields.Boolean (string="É Cliente")
    is_vendor = fields.Boolean (string="É Fornecedor")
    partner_code = fields.Char (string="Codigo")


    
    
    
    
    @api.model 
    def create(self, vals):
        if vals.get('is_client'):
            vals['partner_code'] = self.env['ir.sequence'].next_by_code('res.partner.client')
        if vals.get('is_vendor'):
            vals['partner_code'] = self.env['ir.sequence'].next_by_code('res.partner.vendor')
        if vals.get('is_vendor') and vals.get('is_client'):
            vals['partner_code'] = self.env['ir.sequence'].next_by_code('res.partner.multi')
        res = super(ResPartner, self).create(vals)
        return res


    @api.model
    def write(self, vals):
        if vals.get('is_client'):
            vals['partner_code'] = self.env['ir.sequence'].next_by_code('res.partner.client')
        if vals.get('is_vendor'):
            vals['partner_code'] = self.env['ir.sequence'].next_by_code('res.partner.vendor')
        if vals.get('is_vendor') and vals.get('is_client'):
            vals['partner_code'] = self.env['ir.sequence'].next_by_code('res.partner.multi')
        res = super(ResPartner, self).write(vals)
        return res





    # @api.model
    # def write(self, vals):
    #     if not self.partner_code:
    #         if "is_client" in vals:
    #             self.partner_code = self.env['ir.sequence'].next_by_code('res.partner.client')
    #         if "is_vendor" in vals:
    #             self.partner_code = self.env['ir.sequence'].next_by_code('res.partner.vendor')
    #         if "is_client" in vals or "is_vendor" in vals:
    #             self.partner_code = self.env['ir.sequence'].next_by_code('res.partner.multi')
    #         return super().write(vals) 






            #     vals['partner_code'] = self.env['ir.sequence'].next_by_code('res.partner.client')
            # if vals.get('is_vendor'):
            #     vals['partner_code'] = self.env['ir.sequence'].next_by_code('res.partner.vendor')
            # if vals.get('is_vendor') and vals.get('is_client'):
            #     vals['partner_code'] = self.env['ir.sequence'].next_by_code('res.partner.multi')
            # res = super(ResPartner, self).write(vals)
            # return res



   