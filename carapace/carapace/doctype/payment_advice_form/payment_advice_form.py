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

def updateAmount(doc,method):
	if doc.advice_type == 'Payment Advice Against PO':
		sv = frappe.get_doc("Purchase Order",doc.purchase_order)
		sv.outstanding_amount = doc.outstanding_amount - doc.allocate_amount
		sv.submit()
	if doc.advice_type == 'Service Order':
		sv = frappe.get_doc("Purchase Invoice",doc.purchase_invoice)
		sv.advice_outstanding_amount = doc.outstanding_amount - doc.allocate_amount
		sv.submit()
