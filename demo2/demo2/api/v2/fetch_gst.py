import frappe
import requests
import json
from frappe import _
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def gst_fetch(kwargs):
    try:

        url = "http://127.0.0.1:8000/api/method/demo.demo.sdk.api?version=v1&method=gst_detail&entity=gst_data&id=10001&password=gstnumber001&gst=27AACFZ1876F1ZX"
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.get(url, headers=headers)

        print(response)


    except Exception as e:
        frappe.log_error(f"Error getting gst data: {str(e)}")
        return _("Failed to get gst data.") 