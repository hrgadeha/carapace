from __future__ import unicode_literals
import frappe
from frappe.model.naming import make_autoname
from frappe.model.document import Document

def assign_temp_invoice_no(doc,method):
	name = make_autoname("-.####")
	doc.name = "PR" + name
	doc.proforma_no = doc.name

def rename_invoice(doc,method):
	old_doc = doc.get_doc_before_save()
	frappe.rename_doc(doc.doctype, old_doc.name, make_autoname(doc.naming_series), merge=False)


@frappe.whitelist(allow_guest=True)
def getBankAccount(party_type,party):
	return frappe.db.get_value('Bank Account', {'party_type':party_type,'party':party},
	["name","bank","bank_account_no", "branch_code","swift_number"])