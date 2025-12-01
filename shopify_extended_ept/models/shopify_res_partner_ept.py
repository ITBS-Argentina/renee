from odoo import fields, models, api


class ShopifyResPartnerEpt(models.Model):
	_inherit = "shopify.res.partner.ept"

	@api.model
	def shopify_create_or_update_address(self, shopify_customer_data, parent_partner, partner_type="contact"):
		"""
		Creates or updates existing partner from Shopify customer's data.
		@author: Maulik Barad on Date 09-Sep-2020.
		Overridden method to set company value in vat instead of company_name for task id 42902
		"""
		partner_obj = self.env["res.partner"]

		first_name = shopify_customer_data.get("first_name")
		last_name = shopify_customer_data.get("last_name")

		if not first_name and not last_name:
			return False

		company_name = shopify_customer_data.get("company")
		partner_vals = self.shopify_prepare_partner_vals(shopify_customer_data)
		address_key_list = ["name", "street", "street2", "city", "zip", "phone", "state_id", "country_id"]

		# Added changes here to set company value in vat instead of company_name for task id 42902
		if company_name and str(company_name).isdigit():
			address_key_list.append("vat")
			partner_vals.update({"vat": company_name})
		# Changes end here

		partner = partner_obj._find_partner_ept(partner_vals, address_key_list,
												[("parent_id", "=", parent_partner.id), ("type", "=", partner_type)])

		if not partner:
			partner = partner_obj._find_partner_ept(partner_vals, address_key_list,
													[("parent_id", "=", parent_partner.id)])
		if not partner:
			partner = partner_obj._find_partner_ept(partner_vals, address_key_list)
			if partner and not partner.child_ids and partner_type == 'invoice':
				partner.write({"type": partner_type})
		if partner:
			if parent_partner.email:
				partner.write({'email': parent_partner.email})
			return partner

		partner_vals.update({"type": partner_type, "parent_id": parent_partner.id})
		if parent_partner.email:
			partner_vals.update({'email': parent_partner.email})
		partner = partner_obj.create(partner_vals)
		# Added changes here to set company value in vat instead of company_name for task id 42902
		if company_name and str(company_name).isdigit():
			partner.write({"vat": company_name})
		# Changes end here
		return partner
