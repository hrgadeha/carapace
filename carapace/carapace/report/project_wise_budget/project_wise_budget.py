# Copyright (c) 2013, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _

def execute(filters=None):
	conditions, filters = get_conditions(filters)
	columns = get_column()
	data = get_head(conditions,filters)
	return columns,data

def get_column():
	return [_("Project") + ":Link/Project:250",
		_("Budget Head") + ":Link/Budget Head:250",
		_("Head") + ":Data:150",
		_("Budget") + ":Currency:130",
		_("Committed") + ":Currency:130",
		_("Incurred") + ":Currency:120",
		_("Yet to be committed") + ":Currency:130",
		_("Yet to be Incurred") + ":Currency:150"]

def get_head(conditions,filters):
	budget_head = frappe.db.sql(""" select project,name,head_name,budget,committed,incurred,(budget-committed),
			(committed-incurred) from `tabBudget Head`
			where docstatus is not null %s;"""%conditions, filters, as_list=1)

	return budget_head

def get_conditions(filters):
        conditions = ""
        if filters.get("project"): conditions += "and project = %(project)s"
        if filters.get("head"): conditions += "and head_name = %(head)s"

        return conditions, filters
