frappe.listview_settings['Payment Advice Form'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		if (doc.status === "Closed") {
			return [__("Closed"), "green", "status,=,Closed"];
		} else if (doc.status === "Open") {
			return [__("Open"), "red", "status,=,Open"];
		}
	}
};
