// Copyright (c) 2019, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Payment Advice Form", "make_payment_entry", function(frm){
	var myWin = window.open('http://erp.carapaceinfra.in/desk#Form/Payment%20Entry/New%20Payment%20Entry%201');
});

cur_frm.add_fetch("purchase_order","supplier","party")
cur_frm.add_fetch("purchase_order","transaction_date","po_date")
cur_frm.add_fetch("purchase_order","payment_terms_template","payment_terms_template")
cur_frm.add_fetch("purchase_order","taxes_and_charges","purchase_taxes_and_charges_template")
cur_frm.add_fetch("purchase_order","total","total_amount")
cur_frm.add_fetch("purchase_order","grand_total","grand_total")
cur_frm.add_fetch("purchase_order","total_taxes_and_charges","total_taxes_amount")
cur_frm.add_fetch("purchase_order","outstanding_amount","outstanding_amount")

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

frappe.ui.form.on("Payment Advice Payment Terms", "add", function(frm, cdt, cdn){

	var pterms = frm.doc.payment_advice_payment_terms;
  	var percent = 0;
   	for(var j in pterms) {
		if(pterms[j].add == 1){
		percent = percent + pterms[j].invoice_portion
	}
	}
	
	frm.set_value("payment_percent",percent);
	frm.set_value("allocate",0);
	frm.set_value("add_tax",0);
	frm.set_value("allocate_amount",0);
});

frappe.ui.form.on('Payment Advice Form', {
	allocate: function(frm) {
			var percent = frm.doc.payment_percent;
			var tax = frm.doc.total_taxes_amount;
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
			var tax = frm.doc.total_taxes_amount;
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

frappe.ui.form.on("Payment Advice Form", "onload", function(frm) {
    cur_frm.set_query("purchase_order", function() {
        return {
            "filters": [
                ["Purchase Order", "status", "=", "To Receive and Bill"],
                ["Purchase Order", "outstanding_amount", "!=", 0]
            ]
        };
    });
});

frappe.ui.form.on('Payment Advice Form', {
	"advice_type": function(frm) {
		if (frm.doc.advice_type == "Payment Advice Against PO"){
			frm.set_value("party_type","Supplier");
			frm.set_value("party","");
			frm.set_value("naming_series","PA/PO/.#");
			frm.set_df_property("payment_advice_item","hidden",0);
			frm.set_df_property("payment_terms_template","hidden",0);
			frm.set_df_property("payment_advice_payment_terms","hidden",0);
			frm.set_df_property("purchase_taxes_and_charges_template","hidden",0);
			frm.set_df_property("payment_advice_taxes","hidden",0);
			frm.set_df_property("subject","hidden",1);
			frm.set_df_property("payment_description","hidden",1);
			frm.set_df_property("add_tax","hidden",0);
		}
		else{
			frm.set_value("party_type","Employee");
			frm.set_value("party","");
			frm.set_value("naming_series","PA/EMP/.#");
			frm.set_value("outstanding_amount","");
			frm.set_value("grand_total","");
			frm.set_value("total_amount","");
			frm.set_value("total_taxes_amount","");
			frm.set_value("purchase_order","");
			frm.set_value("po_date","");
			frm.set_value("payment_terms_template","");
			frm.set_value("purchase_taxes_and_charges_template","");
			cur_frm.clear_table("payment_advice_item");
			cur_frm.clear_table("payment_advice_payment_terms");
			cur_frm.clear_table("payment_advice_taxes");
			frm.set_df_property("payment_advice_item","hidden",1);
			frm.set_df_property("payment_terms_template","hidden",1);
			frm.set_df_property("payment_advice_payment_terms","hidden",1);
			frm.set_df_property("purchase_taxes_and_charges_template","hidden",1);
			frm.set_df_property("payment_advice_taxes","hidden",1);
			frm.set_df_property("add_tax","hidden",1);
			frm.set_df_property("subject","hidden",0);
			frm.set_df_property("payment_description","hidden",0);
		}
	}
});

frappe.ui.form.on('Payment Advice Form', 'validate', function(frm) {
    if (frm.doc.allocate_amount > frm.doc.outstanding_amount) {
        msgprint('Allocate Amount Can Not Be Breater Than Outstanding Amount');
        validated = false;
    } 
});

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
			console.log(r.message)
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
