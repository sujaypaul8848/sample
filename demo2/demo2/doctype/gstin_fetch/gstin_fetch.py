# Copyright (c) 2023, sujay paul and contributors
# For license information, please see license.txt


import frappe, requests
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def callfn(**kwargs):

	num = kwargs["gst_number"]

	url= f"http://127.0.0.1:8000/api/method/demo.demo.sdk.api?version=v1&method=gst_detail&entity=gst_data&id=10001&password=gstnumber001&gst={num}"

	response = requests.get(url)
	data = response.json()
	return data["message"]
	# gst = data["message"]["gst_number"]	

	# print(data)
	# print("0")
	# try:
	# 	print("1")
	# 	new_doc = frappe.get_doc("GSTIN_fetch", gst)
	# 	new_doc.gst_number = data["message"]["gst_number"]
	# 	new_doc.business_name = data["message"]["business_name"]
	# 	new_doc.address = data["message"]["address"]
	# 	new_doc.pincode = data["message"]["pincode"]
	# 	new_doc.entity_type = data["message"]["entity_type"]
	# 	new_doc.registration_type = data["message"]["registration_type"]
	# 	new_doc.department_code = data["message"]["department_code"]
	# 	new_doc.nature_of_business = data["message"]["nature_of_business"]
	# 	new_doc.registration_date = data["message"]["registration_date"]
	# 	new_doc.insert()

	# 	frappe.msgprint(f"Record Created Successfully for {data['message']['gst_number']} GST Number")
	# 	return new_doc
	# except Exception as e:
	# 	frappe.msgprint(e)
