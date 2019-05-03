// Copyright (c) 2019, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment Advice Form", "view_ledger", function(frm){
	frappe.route_options = {
 		"party_type": frm.doc.party_type,
 		"party": frm.doc.party
 	};
	frappe.set_route("query-report", "General Ledger");
});

/* ###################################################################################################################################### */

frappe.ui.form.on("Payment Advice Form", "make_payment_entry", function(frm){
	var myWin = window.open('http://erp.carapaceinfra.in/desk#Form/Payment%20Entry/New%20Payment%20Entry%201');
});

/* ###################################################################################################################################### */

cur_frm.add_fetch("purchase_order","supplier","party")
cur_frm.add_fetch("purchase_invoice","supplier","party")
cur_frm.add_fetch("purchase_order","transaction_date","po_date")
cur_frm.add_fetch("purchase_order","payment_terms_template","payment_terms_template")
cur_frm.add_fetch("purchase_order","taxes_and_charges","purchase_taxes_and_charges_template")
cur_frm.add_fetch("purchase_order","total","total_amount")
cur_frm.add_fetch("purchase_order","grand_total","grand_total")
cur_frm.add_fetch("purchase_order","total_taxes_and_charges","total_taxes_amount")
cur_frm.add_fetch("purchase_order","outstanding_amount","outstanding_amount")
cur_frm.add_fetch("purchase_order","project_site","project_site")
cur_frm.add_fetch("purchase_invoice","payment_terms_template","payment_terms_template")
cur_frm.add_fetch("purchase_invoice","taxes_and_charges","purchase_taxes_and_charges_template")
cur_frm.add_fetch("purchase_invoice","total","total_amount")
cur_frm.add_fetch("purchase_invoice","grand_total","grand_total")
cur_frm.add_fetch("purchase_invoice","total_taxes_and_charges","total_taxes_amount")
cur_frm.add_fetch("purchase_invoice","outstanding_amount","outstanding_amount")

/* ###################################################################################################################################### */

frappe.ui.form.on("Payment Advice Form", {
    "purchase_order": function(frm) {
	if (frm.doc.purchase_order){
        frappe.model.with_doc("Purchase Order", frm.doc.purchase_order, function() {
		cur_frm.clear_table("payment_advice_item");
           		var tabletransfer= frappe.model.get_doc("Purchase Order", frm.doc.purchase_order)
           		$.each(tabletransfer.items, function(index, row){
               		var d = frm.add_child("payment_advice_item");
               		d.item_code = row.item_code;
			d.item_name = row.item_name;
			d.qty = row.qty;
			d.rate = row.rate;
			d.amount = row.amount;
               	frm.refresh_field("payment_advice_item");
            });
        });
        
        frappe.model.with_doc("Purchase Order", frm.doc.purchase_order, function() {
		cur_frm.clear_table("payment_advice_payment_terms");
           		var tabletransfer= frappe.model.get_doc("Purchase Order", frm.doc.purchase_order)
           		$.each(tabletransfer.payment_schedule, function(index, row){
               		var d = frm.add_child("payment_advice_payment_terms");
               		d.payment_term = row.payment_term;
			d.description = row.description;
			d.due_date = row.due_date;
			d.invoice_portion = row.invoice_portion;
			d.payment_amount = row.payment_amount;
			d.mode_of_payment = row.mode_of_payment;
               	frm.refresh_field("payment_advice_payment_terms");
            });
        });

	frappe.model.with_doc("Purchase Order", frm.doc.purchase_order, function() {
		cur_frm.clear_table("payment_advice_taxes");
           		var tabletransfer= frappe.model.get_doc("Purchase Order", frm.doc.purchase_order)
           		$.each(tabletransfer.taxes, function(index, row){
               		var d = frm.add_child("payment_advice_taxes");
               		d.type = row.charge_type;
			d.account_head = row.account_head;
			d.rate = row.rate;
			d.amount = row.tax_amount;
			d.total = row.total;
               	frm.refresh_field("payment_advice_taxes");
            });
        });
    }
}
});

frappe.ui.form.on("Payment Advice Form", {
    "purchase_invoice": function(frm) {
	if (frm.doc.purchase_invoice){
        frappe.model.with_doc("Purchase Invoice", frm.doc.purchase_invoice, function() {
		cur_frm.clear_table("payment_advice_item");
           		var tabletransfer= frappe.model.get_doc("Purchase Invoice", frm.doc.purchase_invoice)
           		$.each(tabletransfer.items, function(index, row){
               		var d = frm.add_child("payment_advice_item");
               		d.item_code = row.item_code;
			d.item_name = row.item_name;
			d.qty = row.qty;
			d.rate = row.rate;
			d.amount = row.amount;
               	frm.refresh_field("payment_advice_item");
            });
        });
        
        frappe.model.with_doc("Purchase Invoice", frm.doc.purchase_invoice, function() {
		cur_frm.clear_table("payment_advice_payment_terms");
           		var tabletransfer= frappe.model.get_doc("Purchase Invoice", frm.doc.purchase_invoice)
           		$.each(tabletransfer.payment_schedule, function(index, row){
               		var d = frm.add_child("payment_advice_payment_terms");
               		d.payment_term = row.payment_term;
			d.description = row.description;
			d.due_date = row.due_date;
			d.invoice_portion = row.invoice_portion;
			d.payment_amount = row.payment_amount;
			d.mode_of_payment = row.mode_of_payment;
               	frm.refresh_field("payment_advice_payment_terms");
            });
        });

	frappe.model.with_doc("Purchase Invoice", frm.doc.purchase_invoice, function() {
		cur_frm.clear_table("payment_advice_taxes");
           		var tabletransfer= frappe.model.get_doc("Purchase Invoice", frm.doc.purchase_invoice)
           		$.each(tabletransfer.taxes, function(index, row){
               		var d = frm.add_child("payment_advice_taxes");
               		d.type = row.charge_type;
			d.account_head = row.account_head;
			d.rate = row.rate;
			d.amount = row.tax_amount;
			d.total = row.total;
               	frm.refresh_field("payment_advice_taxes");
            });
        });
    }
}
});

/* ###################################################################################################################################### */

frappe.ui.form.on("Payment Advice Payment Terms", "add", function(frm, cdt, cdn){

	var pterms = frm.doc.payment_advice_payment_terms;
  	var percent = 0;
   	for(var j in pterms) {
		if(pterms[j].add == 1){
		percent = percent + pterms[j].invoice_portion
	}
	}
	
	frm.set_value("payment_percent",percent);
});

/* ###################################################################################################################################### */

frappe.ui.form.on("Payment Advice Taxes", "add", function(frm, cdt, cdn){
	var ptax = frm.doc.payment_advice_taxes;
  	var amount = 0;
   	for(var j in ptax) {
		if(ptax[j].add == 1){
		amount = amount + ptax[j].amount
	}
	}
	
	frm.set_value("total_allocate_tax",amount);
});

/* ###################################################################################################################################### */

frappe.ui.form.on('Payment Advice Form', {
	allocate: function(frm) {
			var percent = frm.doc.payment_percent;
			var tax = frm.doc.total_allocate_tax;
			var allocate_amount = frm.doc.allocate_amount;
			var total = frm.doc.total_amount;
			var grand_total = frm.doc.grand_total;
			var total_with_tax = 0.0;
			var pay = total * (percent/100)
		if(frm.doc.allocate == 1){
				frm.set_value("allocate_amount",pay);
		}
		
		if(frm.doc.allocate == 0){
				frm.set_value("allocate_amount",0);
		}
	},
	add_tax: function(frm) {
			var percent = frm.doc.payment_percent;
			var tax = frm.doc.total_allocate_tax;
			var allocate_amount = frm.doc.allocate_amount;
			var total = frm.doc.total_amount;
			var grand_total = frm.doc.grand_total;
			var total_with_tax = 0.0;
			var pay = 0.0;

			pay = total * (percent/100)
			
		if(frm.doc.allocate == 1 && frm.doc.add_tax == 1){
			total_with_tax = tax + pay;
			frm.set_value("allocate_amount",total_with_tax);
		}
		
		if(frm.doc.add_tax == 0){
			frm.set_value("allocate_amount",pay);
		}
	}
});

/* ###################################################################################################################################### */

frappe.ui.form.on("Payment Advice Form", "onload", function(frm) {
    cur_frm.set_query("purchase_order", function() {
        return {
            "filters": [
                ["Purchase Order", "outstanding_amount", "!=", 0]
            ]
        };
    });
});

frappe.ui.form.on("Payment Advice Form", "onload", function(frm) {
    cur_frm.set_query("purchase_invoice", function() {
        return {
            "filters": [
                ["Purchase Invoice", "advice_outstanding_amount", "!=", 0]
            ]
        };
    });
});

/* ###################################################################################################################################### */

frappe.ui.form.on('Payment Advice Form', {
	"advice_type": function(frm) {
			frm.clear_table("payment_advice_item");
			frm.clear_table("payment_advice_payment_terms");
			frm.clear_table("payment_advice_taxes");
			frm.set_value("purchase_order","");
			frm.set_value("purchase_invoice","");
			frm.set_value("party","");
			frm.set_value("outstanding_amount","");
			frm.set_value("grand_total","");
			frm.set_value("total_amount","");
			frm.set_value("allocate_amount","");
			frm.set_value("add_tax","");
			frm.set_value("allocate","");
			frm.set_value("total_taxes_amount","");
			frm.set_value("po_date","");
			frm.set_value("payment_terms_template","");
			frm.set_value("purchase_taxes_and_charges_template","");
			frm.set_value("project_site","");
			cur_frm.refresh_fields();

		if (frm.doc.advice_type == "Payment Advice Against PO"){
			frm.set_value("party_type","Supplier");
			frm.set_df_property("party_type","read_only",1);
			frm.set_value("naming_series","PA/PO/.#");
			frm.set_df_property("payment_advice_expense","hidden",1);
			frm.set_df_property("payment_advice_item","hidden",0);
			frm.set_df_property("payment_terms_template","hidden",0);
			frm.set_df_property("payment_advice_payment_terms","hidden",0);
			frm.set_df_property("purchase_taxes_and_charges_template","hidden",0);
			frm.set_df_property("payment_advice_taxes","hidden",0);
			frm.set_df_property("subject","hidden",1);
			frm.set_df_property("payment_description","hidden",1);
			frm.set_df_property("add_tax","hidden",0);
		}
		if (frm.doc.advice_type == "Service Order"){
			frm.set_value("party_type","Supplier");
			frm.set_value("naming_series","PA/SO/.#");
			frm.set_df_property("party_type","read_only",1);
			frm.set_df_property("payment_advice_expense","hidden",1);
			frm.set_df_property("payment_advice_item","hidden",0);
			frm.set_df_property("payment_terms_template","hidden",0);
			frm.set_df_property("payment_advice_payment_terms","hidden",0);
			frm.set_df_property("purchase_taxes_and_charges_template","hidden",0);
			frm.set_df_property("payment_advice_taxes","hidden",0);
			frm.set_df_property("subject","hidden",1);
			frm.set_df_property("payment_description","hidden",1);
			frm.set_df_property("add_tax","hidden",0);
			frm.set_df_property("reference_section","hidden",1);
		}
		if (frm.doc.advice_type == "General PA"){
			frm.set_value("naming_series","GPA/.#");
			cur_frm.clear_table("payment_advice_item");
			cur_frm.clear_table("payment_advice_payment_terms");
			cur_frm.clear_table("payment_advice_taxes");
			frm.set_df_property("payment_advice_item","hidden",1);
			frm.set_df_property("party_type","read_only",0);
			frm.set_df_property("project_site","read_only",0);
			frm.set_df_property("payment_advice_expense","hidden",0);
			frm.set_df_property("payment_terms_template","hidden",1);
			frm.set_df_property("payment_advice_payment_terms","hidden",1);
			frm.set_df_property("purchase_taxes_and_charges_template","hidden",1);
			frm.set_df_property("payment_advice_taxes","hidden",1);
			frm.set_df_property("payment_percent","hidden",1);
			frm.set_df_property("add_tax","hidden",1);
			frm.set_df_property("allocate","hidden",1);
			frm.set_df_property("subject","hidden",0);
			frm.set_df_property("payment_description","hidden",0);
		}
	}
});

/* ###################################################################################################################################### */

frappe.ui.form.on('Payment Advice Form', 'validate', function(frm) {
    if (frm.doc.advice_type == "Payment Advice Against PO" && frm.doc.allocate_amount > frm.doc.outstanding_amount) {
        msgprint('Allocate Amount Can Not Be Breater Than Outstanding Amount');
        validated = false;
    } 
});

/* ###################################################################################################################################### */

frappe.ui.form.on('Payment Advice Form', 'payment_type', function(frm) {
	if (frm.doc.payment_type == "Adhoc Payment") {
       		frm.set_df_property("allocate_amount","read_only",0);
    	}
	else{
		frm.set_df_property("allocate_amount","read_only",1);
	}
});

frappe.ui.form.on('Payment Advice Form', 'after_save', function(frm) {
	msgprint("This Party Has Account Balance "+frm.doc.account_balance+ " "+frm.doc.dr_cr)
});

/* ###################################################################################################################################### */

frappe.ui.form.on("Payment Advice Expense", "qty", function(frm, cdt, cdn){
	cur_frm.refresh();
	cur_frm.refresh_fields();
	var d = locals[cdt][cdn];
	var expense = frm.doc.payment_advice_expense;
	var total = 0;
	frappe.model.set_value(d.doctype, d.name, "total", (d.qty * d.rate));
   	for(var j in expense) {
		total = total + expense[j].total;
		frm.set_value("allocate_amount",total);
	}	
});

frappe.ui.form.on("Payment Advice Expense", "rate", function(frm, cdt, cdn){
	cur_frm.refresh();
	cur_frm.refresh_fields();
	var d = locals[cdt][cdn];
	var expense = frm.doc.payment_advice_expense;
	var total = 0;
	frappe.model.set_value(d.doctype, d.name, "total", (d.qty * d.rate));
   	for(var j in expense) {
		total = total + expense[j].total;
		frm.set_value("allocate_amount",total);
	}	
});

frappe.ui.form.on("Payment Advice Expense", "payment_advice_expense_remove", function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var expense = frm.doc.payment_advice_expense;
	var total = 0;
   	for(var j in expense) {
		total = total + expense[j].total;
		frm.set_value("allocate_amount",total);
	}	
	cur_frm.refresh();
	cur_frm.refresh_fields();
});

/* ###################################################################################################################################### */

frappe.ui.form.on('Payment Advice Form', 'party', function(frm) {
	return frappe.call({
		method: "erpnext.accounts.utils.get_balance_on",
		args: {
			date: frm.doc.date, 
			party_type: frm.doc.party_type, 
			party: frm.doc.party
		},
		
		callback: function(r) {
			frm.doc.account_balance = r.message;
			refresh_field('account_balance', 'accounts');
		
		if(r.message > 0){
			frm.set_value("dr_cr","Dr");
		}

		if(r.message < 0){
			frm.set_value("dr_cr","Cr");
		}

		}
	})
});

/* ###################################################################################################################################### */

frappe.ui.form.on("Payment Advice Form", {
  get_details: function(frm) {
    if (frm.doc.purchase_order){
	cur_frm.refresh();
	cur_frm.clear_table("payment_advice_details");
	cur_frm.refresh_fields();
	
    frappe.call({
    "method": "carapace.carapace.doctype.payment_advice_form.payment_advice_form.getPA",
args: {
doctype: "Payment Advice Form",
purchase_order: frm.doc.purchase_order
},
callback:function(r){
	var len=r.message.length;
	for (var i=0;i<len;i++){
	        var row = frm.add_child("payment_advice_details");
		row.payment_advice = r.message[i][0];
		row.outstanding_amount = r.message[i][1];
		row.allocated_amount = r.message[i][2];
		row.percent = r.message[i][3];
		row.tax = r.message[i][4];
	}
		cur_frm.refresh();
	}
    });
}
}
});
