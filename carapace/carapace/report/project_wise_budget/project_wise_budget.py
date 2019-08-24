# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _

def execute(filters=None):
	columns = get_column()
	data = get_silo(filters)
	return columns,data

def get_column():
	return [_("Budget Head") + ":Link/Budget Head:250",_("Head") + ":Data:150",_("Budget") + ":Currency:130",_("Committed") + ":Currency:130",_("Incurred") + ":Currency:120",_("Yet to be committed") + ":Currency:130",_("Yet to be Incurred") + ":Currency:150"]

def get_silo(filters):
	if filters.get("project"):
		project = filters.get("project")
		budget_head = frappe.db.sql(""" select name,head_name,budget,committed,incurred,yet_to_be_committed,yet_to_be_incurred from `tabBudget Head` where project = '%s'; """%(project), as_list=1)

		return budget_head
