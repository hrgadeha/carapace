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
	query="select purchase_order, grand_total, outstanding_amount, allocate_amount from `tabPayment Advice Form` where name = '"+str(payment_advice)+"';"
	li=[]
	dic=frappe.db.sql(query, as_dict=True)
	for i in dic:	
		purchase_order,grand_total,outstanding_amount,allocate_amount=i['purchase_order'],i['grand_total'],i['outstanding_amount'],i['allocate_amount']
		li.append([purchase_order,grand_total,outstanding_amount,allocate_amount])
	return li

@frappe.whitelist(allow_guest=True)
def UpdatePA(doctype, payment_advice = None):
	doc_PA = frappe.get_doc("Payment Advice Form", payment_advice)
	doc_PA.status = "Closed"
	doc_PA.submit()

def updateAmount(doc,method):
	for d in doc.references:
		sv = frappe.get_doc("Purchase Order",d.reference_name)
		sv.outstanding_amount = d.outstanding_amount - d.allocated_amount
		sv.submit()
