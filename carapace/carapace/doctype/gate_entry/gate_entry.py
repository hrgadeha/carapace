# -*- coding: utf-8 -*-
# Copyright (c) 2018, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class GateEntry(Document):
	pass

@frappe.whitelist(allow_guest=True)
def UpdatePO(doctype, po_no = None, name = None):
	doc_po = frappe.get_doc("Purchase Order", po_no)
	doc_po.gate_entry = name
	doc_po.save()

@frappe.whitelist(allow_guest=True)
def UpdateGE(doctype, gate_entry = None, po = None):
	doc_GateEntry = frappe.get_doc("Gate Entry", gate_entry)
	doc_GateEntry.pr_based_po = po
	doc_GateEntry.status = "Closed"
	doc_GateEntry.save()
