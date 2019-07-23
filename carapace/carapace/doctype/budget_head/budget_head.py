# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.naming import make_autoname
from frappe.model.document import Document

class BudgetHead(Document):
	def autoname(self):
		self.name = make_autoname(self.project + '-' + self.head_name + '-')

@frappe.whitelist(allow_guest=True)
def UpdateCommitedPO(doc,method):
	doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
	doc_BH.committed += doc.grand_total
	doc_BH.yet_to_be_committed = doc_BH.budget - doc_BH.committed
	doc_BH.save()

@frappe.whitelist(allow_guest=True)
def UpdateCommited_cancelPO(doc,method):
	doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
	doc_BH.committed -= doc.grand_total
	doc_BH.yet_to_be_committed = doc_BH.budget + doc_BH.committed
	doc_BH.save()

@frappe.whitelist(allow_guest=True)
def UpdateCommited(doc,method):
	if doc.update_budget_head == 1 and (doc.committed_amount != doc.grand_total):
		doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
		doc_BH.committed += doc.grand_total - doc.committed_amount
		doc_BH.yet_to_be_committed = doc_BH.budget - doc_BH.committed
		doc_BH.save()
	elif doc.update_budget_head == 1 and (doc.committed_amount == doc.grand_total):
                doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
                doc_BH.committed += doc.committed_amount
                doc_BH.yet_to_be_committed = doc_BH.budget - doc_BH.committed
                doc_BH.save()


@frappe.whitelist(allow_guest=True)
def UpdateCommited_cancel(doc,method):
	if doc.update_budget_head == 1 and (doc.committed_amount != doc.grand_total):
		doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
		doc_BH.committed -= doc.grand_total - doc.committed_amount
		doc_BH.yet_to_be_committed = doc_BH.budget + doc_BH.committed
		doc_BH.save()
	elif doc.update_budget_head == 1 and (doc.committed_amount == doc.grand_total):
                doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
                doc_BH.committed -= doc.committed_amount
                doc_BH.yet_to_be_committed = doc_BH.budget + doc_BH.committed
                doc_BH.save()


@frappe.whitelist(allow_guest=True)
def UpdatePaid(doc,method):
	doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
	doc_BH.incurred += doc.total_allocated_amount
	doc_BH.yet_to_be_incurred = doc_BH.committed - doc_BH.incurred
	doc_BH.save()

@frappe.whitelist(allow_guest=True)
def UpdatePaid_cancel(doc,method):
	doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
	doc_BH.incurred -= doc.total_allocated_amount
	doc_BH.save()

@frappe.whitelist(allow_guest=True)
def expClaim(doc,method):
	for d in doc.expenses:
		exp = frappe.get_doc("Budget Head",d.budget_head)
		exp.committed -= d.sanctioned_amount
		exp.incurred -= d.sanctioned_amount
		exp.save()
