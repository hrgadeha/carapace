# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.naming import make_autoname
from frappe.model.document import Document

class BudgetHead(Document):
	def autoname(self):
		self.name = make_autoname(self.head_name + '-' + self.project + '-')

@frappe.whitelist(allow_guest=True)
def UpdateCommitedPO(doc,method):
	if doc.budget_head:
		doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
		doc_BH.committed += doc.total
		doc_BH.yet_to_be_committed = doc_BH.budget - doc_BH.committed
		doc_BH.save()

@frappe.whitelist(allow_guest=True)
def UpdateCommited_cancelPO(doc,method):
	if doc.budget_head:
		doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
		doc_BH.committed -= doc.total
		doc_BH.yet_to_be_committed = doc_BH.budget + doc_BH.committed
		doc_BH.save()

@frappe.whitelist(allow_guest=True)
def UpdateCommited(doc,method):
	if doc.update_budget_head == 1:
		for bh in doc.items:
                        exp = frappe.get_doc("Budget Head",bh.budget_head)
                        exp.committed += bh.amount
                        exp.yet_to_be_committed = exp.budget - exp.committed
                        exp.save()

@frappe.whitelist(allow_guest=True)
def UpdateCommited_cancel(doc,method):
        if doc.update_budget_head == 1:
                for bh in doc.items:
                        exp = frappe.get_doc("Budget Head",bh.budget_head)
                        exp.committed -= bh.amount
                        exp.yet_to_be_committed = exp.budget + exp.committed
                        exp.save()

@frappe.whitelist(allow_guest=True)
def UpdatePaid(doc,method):
	if doc.budget_head:
		doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
		doc_BH.incurred += doc.total
		doc_BH.yet_to_be_incurred = doc_BH.committed - doc_BH.incurred
		doc_BH.save()

	if doc.voucher_no:
                for bh in doc.budget_table:
                        exp = frappe.get_doc("Budget Head",bh.budget_head)
                        exp.incurred += bh.amount
                        exp.yet_to_be_incurred = exp.committed - exp.incurred
                        exp.save()

@frappe.whitelist(allow_guest=True)
def UpdatePaid_cancel(doc,method):
	if doc.budget_head:
		doc_BH = frappe.get_doc("Budget Head", doc.budget_head)
		doc_BH.incurred -= doc.total
		doc_BH.yet_to_be_incurred = doc_BH.committed + doc_BH.incurred
		doc_BH.save()

	if doc.voucher_no:
                for bh in doc.budget_table:
                        exp = frappe.get_doc("Budget Head",bh.budget_head)
                        exp.incurred -= bh.amount
                        exp.yet_to_be_incurred = exp.committed + exp.incurred
                        exp.save()

@frappe.whitelist(allow_guest=True)
def expClaim(doc,method):
	for d in doc.expenses:
		if d.budget_head:
			exp = frappe.get_doc("Budget Head",d.budget_head)
			exp.committed -= d.sanctioned_amount
			exp.incurred -= d.sanctioned_amount
			exp.save()

@frappe.whitelist(allow_guest=True)
def jvBudget(doc,method):
	for bh in doc.accounts:
		if bh.debit_in_account_currency != 0 and bh.budget_head:
			exp = frappe.get_doc("Budget Head",bh.budget_head)
			exp.committed += bh.debit_in_account_currency
			exp.yet_to_be_committed = exp.budget - exp.committed
			exp.save()

@frappe.whitelist(allow_guest=True)
def jvBudget_cancel(doc,method):
	for bh in doc.accounts:
		if bh.debit_in_account_currency != 0 and bh.budget_head:
			exp = frappe.get_doc("Budget Head",bh.budget_head)
			exp.committed -= bh.debit_in_account_currency
			exp.yet_to_be_committed = exp.budget + exp.committed
			exp.save()

@frappe.whitelist(allow_guest=True)
def createSS(doc,method):
        for bh in doc.project_and_budget_allocation:
                if bh.budget_head:
                        exp = frappe.get_doc("Budget Head",bh.budget_head)
                        exp.committed += bh.amount
                        exp.yet_to_be_committed = exp.budget - exp.committed
                        exp.save()

@frappe.whitelist(allow_guest=True)
def cancelSS(doc,method):
        for bh in doc.project_and_budget_allocation:
                if bh.budget_head:
                        exp = frappe.get_doc("Budget Head",bh.budget_head)
                        exp.committed -= bh.amount
                        exp.yet_to_be_committed = exp.budget + exp.committed
                        exp.save()

@frappe.whitelist(allow_guest=True)
def insertSS(doc,method):
        for bh in doc.project_and_budget_allocation:
                bh.project = "FINAL TEST PROJECT N-001"
		bh.budget_head = "Salary & Wages-FINAL TEST PROJECT N-001-00001"
		bh.percent = 100
