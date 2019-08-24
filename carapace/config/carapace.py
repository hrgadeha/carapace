from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Gate Pass"),
			"items": [
				{
					"type": "doctype",
					"name": "Gate Entry",
					"label": "Gate Entry",
					"description": _("Gate Entry"),
				},
				{
					"type": "doctype",
					"name": "Gate Entry Type",
					"label": "Gate Entry Type",
					"description": _("Gate Entry Type"),
				},
				{
					"type": "doctype",
					"name": "Project Site",
					"label": _("Project Site"),
					"description": _("Project Site"),
				},
			]
		},
		{
			"label": _("Budget Management"),
			"items": [
				{
					"type": "doctype",
					"name": "Head",
					"label": _("Head"),
					"description": _("Head"),
				},
				{
                                        "type": "doctype",
                                        "name": "Budget Head",
                                        "label": _("Budget Head"),
                                        "description": _("Budget Head"),
                                },
			]
		},
		{
                        "label": _("Payment Management"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Payment Advice Form",
                                        "label": _("Payment Advice Form"),
                                        "description": _("Payment Advice Form"),
                                },
                        ]
                },
		{
                        "label": _("Budget Report"),
                        "items": [
                                {
					"type": "report",
					"is_query_report": True,
					"name": "Project Wise budget",
					"doctype": "Budget Head"
				},
                        ]
                }
	]
