// Copyright (c) 2018, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gate Entry', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on('Gate Entry', {
	"type_of_vehicle": function(frm) {
		frm.set_value("contact_number","");
		frm.set_value("vehicle_number","");
		frm.set_value("driver_name","");
	}
});

frappe.ui.form.on('Gate Entry', {
	"bill_or_challan": function(frm) {
		frm.set_value("bill_no","");
		frm.set_value("challan_no","");
		frm.set_value("bill_date","");
		frm.set_value("challan_date","");
	}
});

frappe.ui.form.on("Gate Entry", "onload", function(frm) {
    cur_frm.set_query("po_no", function() {
        return {
            "filters": {
                "project_site": frm.doc.project_site_name
            }
        };
    });
});

frappe.ui.form.on("Gate Entry", "onload", function(frm) {
    cur_frm.set_query("returnable_po", function() {
        return {
            "filters": {
                "project_site": frm.doc.project_site_name
            }
        };
    });
});

frappe.ui.form.on("Gate Entry", "onload", function(frm) {
    cur_frm.set_query("po_no_manual", function() {
        return {
            "filters": {
                "project_site": frm.doc.project_site_name
            }
        };
    });
});

frappe.ui.form.on("Gate Entry", "onload", function(frm) {
    cur_frm.set_query("purchase_receipt_no", function() {
        return {
            "filters": {
                "po": frm.doc.po_no_manual,
		"status": "To Bill"
            }
        };
    });
});

frappe.ui.form.on('Gate Entry', {
	"edit_po_date": function(frm) {
		if (frm.doc.edit_po_date == 1){
			frm.set_df_property("posting_date","read_only",0);
			frm.set_df_property("posting_time","read_only",0);
		}
		else{
			frm.set_df_property("posting_date","read_only",1);
			frm.set_df_property("posting_time","read_only",1);
		}
	}
});

frappe.ui.form.on('Gate Entry', {
	"gate_entry_type": function(frm) {
		if (frm.doc.gate_entry_type == "Rejection By ERP"){
			frm.set_df_property("po_no_manual","reqd",1);
			frm.set_df_property("purchase_receipt_no","reqd",1);
		}
		else if (frm.doc.gate_entry_type == "Manual Rejection"){
			frm.set_df_property("rejection_po","reqd",1);
			frm.set_df_property("rejection_purchase_receipt_no","reqd",1);
		}
		else{
			frm.set_df_property("po_no_manual","reqd",0);
			frm.set_df_property("purchase_receipt_no","reqd",0);
			frm.set_df_property("rejection_po","reqd",0);
			frm.set_df_property("rejection_purchase_receipt_no","reqd",0);
		}
	}
});

frappe.ui.form.on('Gate Entry', {
	"gate_entry_type": function(frm) {
		frm.set_value("po_no","");
		frm.set_value("po_no_manual","");
		frm.set_value("purchase_receipt_no","");
		frm.set_value("po_date","");
		frm.set_value("supplier_name","");
		if (frm.doc.po_no == ""){
			cur_frm.clear_table("gate_entry_items");
	               	frm.refresh_field("gate_entry_items");
		}
	}
});

cur_frm.add_fetch("po_no","transaction_date","po_date")
cur_frm.add_fetch("po_no_manual","transaction_date","po_date")
cur_frm.add_fetch("po_no","supplier","supplier_name")
cur_frm.add_fetch("po_no_manual","supplier","supplier_name")
cur_frm.add_fetch("returnable_po","supplier","supplier_name")
cur_frm.add_fetch("returnable_po","transaction_date","po_date")


frappe.ui.form.on("Gate Entry", {
    "purchase_receipt_no": function(frm) {
	if (frm.doc.purchase_receipt_no!= ""){
        	frappe.model.with_doc("Purchase Receipt", frm.doc.purchase_receipt_no, function() {
		cur_frm.clear_table("rejection_gate_entry_items");
            		var tabletransfer= frappe.model.get_doc("Purchase Receipt", frm.doc.purchase_receipt_no)
            		$.each(tabletransfer.items, function(index, row){
				if(row.rejected_qty != 0){
                		var d = frm.add_child("rejection_gate_entry_items");
                		d.item_code = row.item_code;
				d.item_name = row.item_name;
				d.qty = row.received_qty;
				d.rejected_qty = row.rejected_qty;
				d.uom = row.uom;
				d.description = row.description;
                	frm.refresh_field("rejection_gate_entry_items");
			}
            });
        });
    }
}
});

frappe.ui.form.on("Gate Entry", {
    "po_no": function(frm) {
	if (frm.doc.po_no!= ""){
        	frappe.model.with_doc("Purchase Order", frm.doc.po_no, function() {
		cur_frm.clear_table("gate_entry_items");
            		var tabletransfer= frappe.model.get_doc("Purchase Order", frm.doc.po_no)
            		$.each(tabletransfer.items, function(index, row){
                		var d = frm.add_child("gate_entry_items");
                		d.item_code = row.item_code;
				d.item_name = row.item_name;
				d.qty = row.qty;
				d.uom = row.uom;
				d.description = row.description;
                	frm.refresh_field("gate_entry_items");
            });
        });
    }
}
});
