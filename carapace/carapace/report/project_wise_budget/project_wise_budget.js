// Copyright (c) 2016, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Project Wise budget"] = {
	"filters": [
		{
        	    "fieldname": "project",
       		    "label": __("Select Project"),
        	    "fieldtype": "Link",
		    "options": "Project"
        	},
		{
                    "fieldname": "head",
                    "label": __("Select Head"),
                    "fieldtype": "Link",
                    "options": "Head"
                }
	]
}
