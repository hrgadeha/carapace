# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "carapace"
app_title = "Carapace"
app_publisher = "frappe"
app_description = "App For Carapace Infra"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "frappe@io"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/carapace/css/carapace.css"
# app_include_js = "/assets/carapace/js/carapace.js"

# include js, css files in header of web template
# web_include_css = "/assets/carapace/css/carapace.css"
# web_include_js = "/assets/carapace/js/carapace.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "carapace.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "carapace.install.before_install"
# after_install = "carapace.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "carapace.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Payment Advice Form": {
		"on_submit": "carapace.carapace.doctype.payment_advice_form.payment_advice_form.updateAmount"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"carapace.tasks.all"
# 	],
# 	"daily": [
# 		"carapace.tasks.daily"
# 	],
# 	"hourly": [
# 		"carapace.tasks.hourly"
# 	],
# 	"weekly": [
# 		"carapace.tasks.weekly"
# 	]
# 	"monthly": [
# 		"carapace.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "carapace.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "carapace.event.get_events"
# }

