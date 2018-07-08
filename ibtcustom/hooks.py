# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ibtcustom"
app_title = "IBTCustom"
app_publisher = "Finbyz Tech Pvt Ltd"
app_description = "Customizations for IBT"
app_icon = "octicon octicon-file-directory"
app_color = "#008000"
app_email = "info@finbyz.com"
app_license = "GPL 3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ibtcustom/css/ibtcustom.css"
app_include_css = "/assets/ibtcustom/css/ibtcustom.min.css"
# app_include_js = "/assets/ibtcustom/js/ibtcustom.js"
app_include_js = "/assets/ibtcustom/js/ibtcustom.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/ibtcustom/css/ibtcustom.css"
# web_include_js = "/assets/ibtcustom/js/ibtcustom.js"

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
# get_website_user_home_page = "ibtcustom.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ibtcustom.install.before_install"
# after_install = "ibtcustom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ibtcustom.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ibtcustom.tasks.all"
# 	],
# 	"daily": [
# 		"ibtcustom.tasks.daily"
# 	],
# 	"hourly": [
# 		"ibtcustom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ibtcustom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ibtcustom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ibtcustom.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ibtcustom.event.get_events"
# }

email_append_to = ["HR Issue", "Admin Issue"]


doc_events = {
	"Sales Order": {
		"on_submit": "ibtcustom.api.so_on_submit",
		"on_cancel": "ibtcustom.api.so_on_cancel"	
	},
	"Quotation": {
		"on_submit": "ibtcustom.api.qt_on_submit",
		"on_cancel": "ibtcustom.api.qt_on_cancel",
		"on_update_after_submit": "ibtcustom.api.qt_on_update"
	},
	"Auto Email Report": {
		"before_insert": "ibtcustom.api.override_validate"
	},
	"Opportunity": {
		"before_save": "ibtcustom.api.opp_before_save"
	},
	"Lead": {
		"on_update": "ibtcustom.api.update_lead_owner"
	},
	"Employee Handover": {
		"on_submit": "ibtcustom.api.er_on_submit",
		"on_cancel": "ibtcustom.api.er_on_cancel"
	},
	"Salary Slip": {
		"before_save": "ibtcustom.api.sl_before_save"
	},	
	"Employee Loan Application" : {
		"validate": "ibtcustom.api.ela_validate"
	}
}

scheduler_events = {
	"hourly": [
		"ibtcustom.api.change_email_status"
	],
	"daily": [
		"ibtcustom.api.employee_birthday_mails",
		"ibtcustom.api.daily_task_report",
		"ibtcustom.api.make_todo",
		"ibtcustom.api.update_issue_status",
		"ibtcustom.api.daily_leave_allocation"
	],
	"weekly": [
		"ibtcustom.api.sales_invoice_mails",
		"ibtcustom.api.weekly_reports"
	],
	"monthly": [
		"ibtcustom.api.monthly_leave_allocation"
	],	
	"yearly": [
		"ibtcustom.api.yearly_leave_allocation"
	]
}