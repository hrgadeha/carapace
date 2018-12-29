// Copyright (c) 2018, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gate Entry', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on('Gate Entry', {
	"material_against_po_no": function(frm) {
		frm.set_value("po_no","");
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

frappe.ui.form.on("Gate Entry", {
    "po_no": function(frm) {
	if (frm.doc.po_no!= ""){
        	frappe.model.with_doc("Purchase Order", frm.doc.po_no, function() {
		cur_frm.clear_table("gate_entry_items");
            		var tabletransfer= frappe.model.get_doc("Purchase Order", frm.doc.po_no)
            		$.each(tabletransfer.items, function(index, row){
                		var d = frm.add_child("gate_entry_items");
				console.log(row.item_code)
                		d.item_code = row.item_code;
				d.item_name = row.item_name;
				d.description = row.description;
                	frm.refresh_field("gate_entry_items");
            });
        });
    }
}
});
