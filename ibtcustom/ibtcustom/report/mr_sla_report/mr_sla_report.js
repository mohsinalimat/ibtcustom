// Copyright (c) 2016, Finbyz Tech Pvt Ltd and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["MR SLA Report"] = {
	"filters": [
		{
			fieldname: "from_date",
			label:__("From Date"),
			fieldtype: "Date",
			default : frappe.datetime.add_days(frappe.datetime.nowdate(), -30),
			reqd: 1
		},
		{
			fieldname: "to_date",
			label:__("To Date"),
			fieldtype: "Date",
			default : frappe.datetime.nowdate(),
			reqd: 1
		}
	]
}
