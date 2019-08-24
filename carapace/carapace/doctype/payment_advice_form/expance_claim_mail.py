# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

############################################################################################################################################

@frappe.whitelist(allow_guest=True)
def sendMail_Draft(doc,method):
	if doc.workflow_state == 'Applied':
		content = "<h4>Hello,</h4><h2>Kind Attention : Accountant,</h2><p>Please release the payment against Expense Claim.</p><br><h4><center><b>Expense Claim</b></center></h4><table class='table table-bordered'><table class='table table-bordered'><tr><td>Employee Name : "+str(doc.employee_name)+"</td></tr><tr><td>Department : "+str(doc.department)+"</td></tr><tr><td>Expense Approver : "+str(doc.expense_approver)+"</td></tr><tr><td>Status : "+str(doc.workflow_state)+"</td></tr><tr><td>Date : "+str(doc.posting_date)+"</td></tr><tr><td>Remark : "+str(doc.remark)+"</td></tr></table>"

		content = content + "<h4><b>Expense Details</b></h4><table class='table table-bordered'><tr><th>Expense Date</th><th>Expense Claim Type</th><th>Description</th><th>Claim Amount</th><th>Sanctioned Amount</th></tr>"

		for item in doc.expenses:
			expense_date = item.expense_date
			expense_type = item.expense_type
			description = item.description
			claim_amount = item.claim_amount
			sanctioned_amount = item.sanctioned_amount
			content = content + "<tr><td>"+str(expense_date)+"</td><td>"+str(expense_type)+"</td><td>"+str(description)+"</td><td>"+str(claim_amount)+"</td><td>"+str(sanctioned_amount)+"</td></tr>"

		content = content + "</table>"
		content = content + "<br><table class='table table-bordered'><tr><td>Total Claimed Amount : "+str('{:20,.2f}'.format(doc.total_claimed_amount))+"</td><td>Total Sanctioned Amount : "+str(doc.total_sanctioned_amount)+"</td></tr></table></table>"
		section = " | "
		subject = str(doc.name) + section + str(doc.employee_name) + section + str('{:20,.2f}'.format(doc.total_claimed_amount))
		frappe.sendmail(recipients="accounts@carapaceinfra.in",sender="erpnext.notifications@carapaceinfra.com",subject=subject, content=content)

	if doc.workflow_state == 'Created by Employee':
		content = "<h4>Hello,</h4><h2>Kind Attention : Account manager,</h2><p>Please release the payment against Expense Claim.</p><br><h4><center><b>Expense Claim</b></center></h4><table class='table table-bordered'><table class='table table-bordered'><tr><td>Employee Name : "+str(doc.employee_name)+"</td></tr><tr><td>Department : "+str(doc.department)+"</td></tr><tr><td>Expense Approver : "+str(doc.expense_approver)+"</td></tr><tr><td>Status : "+str(doc.workflow_state)+"</td></tr><tr><td>Date : "+str(doc.posting_date)+"</td></tr><tr><td>Remark : "+str(doc.remark)+"</td></tr></table>"

		content = content + "<h4><b>Expense Details</b></h4><table class='table table-bordered'><tr><th>Expense Date</th><th>Expense Claim Type</th><th>Description</th><th>Claim Amount</th><th>Sanctioned Amount</th></tr>"

		for item in doc.expenses:
			expense_date = item.expense_date
			expense_type = item.expense_type
			description = item.description
			claim_amount = item.claim_amount
			sanctioned_amount = item.sanctioned_amount
			content = content + "<tr><td>"+str(expense_date)+"</td><td>"+str(expense_type)+"</td><td>"+str(description)+"</td><td>"+str(claim_amount)+"</td><td>"+str(sanctioned_amount)+"</td></tr>"

		content = content + "</table>"
		content = content + "<br><table class='table table-bordered'><tr><td>Total Claimed Amount : "+str('{:20,.2f}'.format(doc.total_claimed_amount))+"</td><td>Total Sanctioned Amount : "+str(doc.total_sanctioned_amount)+"</td></tr></table></table>"
		section = " | "
		subject = str(doc.name) + section + str(doc.employee_name) + section + str('{:20,.2f}'.format(doc.total_claimed_amount))
		frappe.sendmail(recipients="ketan@finbridge.co.in",sender="erpnext.notifications@carapaceinfra.com",subject=subject, content=content)

	if doc.workflow_state == 'Approved by Account Manager':
		content = "<h4>Hello,</h4><h2>Kind Attention : Naveen Sharma,</h2><p>Please release the payment against Expense Claim.</p><br><h4><center><b>Expense Claim</b></center></h4><table class='table table-bordered'><table class='table table-bordered'><tr><td>Employee Name : "+str(doc.employee_name)+"</td></tr><tr><td>Department : "+str(doc.department)+"</td></tr><tr><td>Expense Approver : "+str(doc.expense_approver)+"</td></tr><tr><td>Status : "+str(doc.workflow_state)+"</td></tr><tr><td>Date : "+str(doc.posting_date)+"</td></tr><tr><td>Remark : "+str(doc.remark)+"</td></tr></table>"

		content = content + "<h4><b>Expense Details</b></h4><table class='table table-bordered'><tr><th>Expense Date</th><th>Expense Claim Type</th><th>Description</th><th>Claim Amount</th><th>Sanctioned Amount</th></tr>"

		for item in doc.expenses:
			expense_date = item.expense_date
			expense_type = item.expense_type
			description = item.description
			claim_amount = item.claim_amount
			sanctioned_amount = item.sanctioned_amount
			content = content + "<tr><td>"+str(expense_date)+"</td><td>"+str(expense_type)+"</td><td>"+str(description)+"</td><td>"+str(claim_amount)+"</td><td>"+str(sanctioned_amount)+"</td></tr>"

		content = content + "</table>"
		content = content + "<br><table class='table table-bordered'><tr><td>Total Claimed Amount : "+str('{:20,.2f}'.format(doc.total_claimed_amount))+"</td><td>Total Sanctioned Amount : "+str(doc.total_sanctioned_amount)+"</td></tr></table></table>"
		section = " | "
		subject = str(doc.name) + section + str(doc.employee_name) + section + str('{:20,.2f}'.format(doc.total_claimed_amount))
		frappe.sendmail(recipients="Naveen.sharma@carapaceinfra.in",sender="erpnext.notifications@carapaceinfra.com",subject=subject, content=content)

############################################################################################################################################

def sendMail_Approved(doc,method):
	content = "<h4>Hello,</h4><h2>Kind Attention: Mr. Souvik Das / Mr. Vivek Sharma,</h2><p>Please release the payment against Expense Claim.</p><br><h4><center><b>Expense Claim</b></center></h4><table class='table table-bordered'><table class='table table-bordered'><tr><td>Employee Name : "+str(doc.employee_name)+"</td></tr><tr><td>Department : "+str(doc.department)+"</td></tr><tr><td>Expense Approver : "+str(doc.expense_approver)+"</td></tr><tr><td>Status : "+str(doc.workflow_state)+"</td></tr><tr><td>Remark : "+str(doc.remark)+"</td></tr></table>"

	content = content + "<h4><b>Expense Details</b></h4><table class='table table-bordered'><tr><th>Expense Date</th><th>Expense Claim Type</th><th>Description</th><th>Claim Amount</th><th>Sanctioned Amount</th></tr>"

	for item in doc.expenses:
		if item.budget_head:
			exp = frappe.get_doc("Budget Head",item.budget_head)
			exp.committed += item.sanctioned_amount
			exp.incurred += item.sanctioned_amount
			exp.save()
		expense_date = item.expense_date
		expense_type = item.expense_type
		description = item.description
		claim_amount = item.claim_amount
		sanctioned_amount = item.sanctioned_amount
		content = content + "<tr><td>"+str(expense_date)+"</td><td>"+str(expense_type)+"</td><td>"+str(description)+"</td><td>"+str(claim_amount)+"</td><td>"+str(sanctioned_amount)+"</td></tr>"

	content = content + "</table>"
	content = content + "<br><table class='table table-bordered'><tr><td>Total Claimed Amount : "+str('{:20,.2f}'.format(doc.total_claimed_amount))+"</td><td>Total Sanctioned Amount : "+str(doc.total_sanctioned_amount)+"</td></tr></table></table>"
	section = " | "
	subject = str(doc.name) + section + str(doc.employee_name) + section + str('{:20,.2f}'.format(doc.total_claimed_amount))
	frappe.sendmail(recipients=["Souvik.das@carapaceinfra.in","vivek.sharma@carapaceinfra.in","naveen.sharma@carapaceinfra.in","rinu.kori@carapaceinfra.com","Accounts@carapaceinfra.in","sandeep.saluja@carapaceinfra.in","ketan@finbridge.co.in"],sender="erpnext.notifications@carapaceinfra.com",subject=subject, content=content)







