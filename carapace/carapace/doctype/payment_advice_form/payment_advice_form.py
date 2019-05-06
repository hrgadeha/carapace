# -*- coding: utf-8 -*-
# Copyright (c) 2019, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PaymentAdviceForm(Document):
	pass

@frappe.whitelist(allow_guest=True)
def insert_data(doctype, payment_advice):
	query="select reference_type,reference_no , grand_total, outstanding_amount, allocate_amount from `tabPayment Advice Form` where name = '"+str(payment_advice)+"';"
	li=[]
	dic=frappe.db.sql(query, as_dict=True)
	for i in dic:
		reference_type,reference_no,grand_total,outstanding_amount,allocate_amount=i['reference_type'],i['reference_no'],i['grand_total'],i['outstanding_amount'],i['allocate_amount']
		li.append([reference_type,reference_no,grand_total,outstanding_amount,allocate_amount])
	return li

@frappe.whitelist(allow_guest=True)
def getPA(doctype, purchase_order):
	query="select name, outstanding_amount, allocate_amount, payment_percent,add_tax from `tabPayment Advice Form` where purchase_order = '"+str(purchase_order)+"' ORDER BY name desc;"
	li=[]
	dic=frappe.db.sql(query, as_dict=True)
	for i in dic:
		name,outstanding_amount,allocate_amount,payment_percent,add_tax=i['name'],i['outstanding_amount'],i['allocate_amount'],i['payment_percent'],i['add_tax']
		li.append([name,outstanding_amount,allocate_amount,payment_percent,add_tax])
	return li

@frappe.whitelist(allow_guest=True)
def UpdatePA(doctype, payment_advice = None):
	doc_PA = frappe.get_doc("Payment Advice Form", payment_advice)
	doc_PA.status = "Closed"
	doc_PA.submit()

@frappe.whitelist(allow_guest=True)
def updateAmount(reference_type = None, reference_no = None, outstanding_amount = None, allocate_amount = None, diff = None):
	ref = frappe.get_doc(reference_type,reference_no)
	ref.advice_outstanding_amount = diff
	ref.submit()

def sendMail(doc,method):
	if doc.advice_type != 'General PA':
		content = "<h4>Hello,</h4><p>Please Proceed Payment Against Payment Advice.</p><br><h4><center><b>Payment Advice</b></center></h4><table class='table table-bordered'><table class='table table-bordered'><tr><td>Party Type : "+str(doc.party_type)+"</td><td>Payment Advice : "+str(doc.name)+"</td></tr><tr><td>Party : "+str(doc.party)+"</td><td>Advice Date: "+str(doc.date)+"</td></tr><tr><td>Reference Type : "+str(doc.reference_type)+"</td><td></td></tr><tr><td>Reference No : "+str(doc.reference_no)+"</td><td></td></tr><tr><td>Project Site : "+str(doc.project_site)+"</td><td></td></tr><tr><td>Payment Type : "+str(doc.payment_type)+"</td><td></td></tr></table>"

		content = content + "<h4><b>Item Details</b></h4><table class='table table-bordered'><tr><th>Item Code</th><th>Item Name</th><th>Qty</th><th>Rate</th><th>Amount</th></tr>"

		for item in doc.payment_advice_item:
			item_code = item.item_code
			item_name = item.item_name
			qty = '{:20,.2f}'.format(item.qty)
			rate = '{:20,.2f}'.format(item.rate)
			amount = '{:20,.2f}'.format(item.amount)
			content = content + "<tr><td>"+str(item_code)+"</td><td>"+str(item_name)+"</td><td>"+str(qty)+"</td><td>"+str(rate)+"</td><td>"+str(amount)+"</td></tr>"
		content = content + "</table><h4><b>Payment Terms : "+str(doc.payment_terms_template)+"</b></h4><table class='table table-bordered'><tr><th>Payment Term</th><th>Description</th><th>Due Date</th><th>Invoice Portion</th><th>Payment Amount</th></tr>"

		for terms in doc.payment_advice_payment_terms:
			payment_term = terms.payment_term
			description = terms.description
			due_date = terms.due_date
			invoice_portion = terms.invoice_portion
			payment_amount = '{:20,.2f}'.format(terms.payment_amount)
			content = content + "<tr><td>"+str(payment_term)+"</td><td>"+str(description)+"</td><td>"+str(due_date)+"</td><td>"+str(invoice_portion)+" %</td><td>"+str(payment_amount)+"</td></tr>"
		content = content + "</table><h4><b>Taxes And Charges : "+str(doc.purchase_taxes_and_charges_template)+"</b></h4><table class='table table-bordered'><tr><th>Type</th><th>Account Head</th><th>Rate</th><th>Amount</th><th>Total</th></tr>"

		for tax in doc.payment_advice_taxes:
			type = tax.type
			account_head = tax.account_head
			rate = '{:20,.2f}'.format(tax.rate)
			amount = '{:20,.2f}'.format(tax.amount)
			total = '{:20,.2f}'.format(tax.total)
			content = content + "<tr><td>"+str(type)+"</td><td>"+str(account_head)+"</td><td>"+str(rate)+" %</td><td>"+str(amount)+"</td><td>"+str(total)+"</td></tr>"
		content = content + "</table>"
		content = content + "<br><table class='table table-bordered'><tr><td>Total Amount : "+str('{:20,.2f}'.format(doc.total_amount))+"</td><td>Payment Percent : "+str(doc.payment_percent)+" %</td></tr><tr><td>Total Taxes Amount : "+str('{:20,.2f}'.format(doc.total_taxes_amount))+"</td><td>To Pay: "+str('{:20,.2f}'.format(doc.allocate_amount))+"</td></tr><tr><td>Total Allocate Tax : "+str('{:20,.2f}'.format(doc.total_allocate_tax))+"</td><td>Account Balance : "+str('{:20,.2f}'.format(doc.account_balance))+" "+str(doc.dr_cr)+"</td></tr><tr><td>Grand Total : "+str('{:20,.2f}'.format(doc.grand_total))+"</td><td></td></tr><tr><td>Outstanding Amount : "+str('{:20,.2f}'.format(doc.outstanding_amount))+"</td><td></td></tr></table></table>"
		recipient = doc.user_id
		section = " | "
		subject = str(doc.name) + section + str(doc.party) + section + str('{:20,.2f}'.format(doc.allocate_amount)) + section + str(doc.project_site)
		frappe.sendmail(recipients=recipient,sender="hardikgadesha@gmail.com",subject=subject, content=content)
	
	else:
		content = "<h4>Hello,</h4><p>Please Proceed Payment Against Payment Advice.</p><br><h4><center><b>Payment Advice</b></center></h4><table class='table table-bordered'><table class='table table-bordered'><tr><td>Party Type : "+str(doc.party_type)+"</td><td>Payment Advice : "+str(doc.name)+"</td></tr><tr><td>Party : "+str(doc.party)+"</td><td>Advice Date: "+str(doc.date)+"</td></tr><tr><td>Reference Type : "+str(doc.reference_type)+"</td><td></td></tr><tr><td>Reference No : "+str(doc.reference_no)+"</td><td></td></tr><tr><td>Project Site : "+str(doc.project_site)+"</td><td></td></tr><tr><td>Payment Type : "+str(doc.payment_type)+"</td><td></td></tr></table>"

		content = content + "<h4><b>Expense Description</b></h4><table class='table table-bordered'><tr><th>Expense Description</th><th>Project Site</th><th>UOM</th><th>Qty</th><th>Rate</th><th>Amount</th></tr>"

		for item in doc.payment_advice_expense:
			expense_description = item.expense_description
			project_site = item.project_site
			uom = item.uom
			qty = '{:20,.2f}'.format(item.qty)
			rate = '{:20,.2f}'.format(item.rate)
			total = '{:20,.2f}'.format(item.total)
			content = content + "<tr><td>"+str(expense_description)+"</td><td>"+str(project_site)+"</td><td>"+str(uom)+"</td><td>"+str(qty)+"</td><td>"+str(rate)+"</td><td>"+str(total)+"</td></tr>"
		content = content + "</table>"
		content = content + "<br><table class='table table-bordered'><tr><td>To Pay: "+str('{:20,.2f}'.format(doc.allocate_amount))+"</td></tr><td>Account Balance : "+str('{:20,.2f}'.format(doc.account_balance))+" "+str(doc.dr_cr)+"</td></table></table>"
		recipient = doc.user_id
		section = " | "
		subject = str(doc.name) + section + str(doc.party) + section + str('{:20,.2f}'.format(doc.allocate_amount)) + section + str(doc.project_site)
		frappe.sendmail(recipients=recipient,sender="erpnext.notifications@carapaceinfra.com",subject=subject, content=content)
