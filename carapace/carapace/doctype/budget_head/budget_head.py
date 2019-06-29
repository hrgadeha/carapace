# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BudgetHead(Document):
	pass

@frappe.whitelist(allow_guest=True)
def UpdateCommited(doc,method):
	doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
	doc_BH.committed += doc.grand_total
	doc_BH.yet_to_be_committed = doc_BH.budget - doc_BH.committed
	doc_BH.save()

@frappe.whitelist(allow_guest=True)
def UpdatePaid(doc,method):
	doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
	doc_BH.incurred += doc.total_allocated_amount
	doc_BH.yet_to_be_incurred = doc_BH.committed - doc_BH.incurred
	doc_BH.save()
