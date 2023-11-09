// Copyright (c) 2023, sujay paul and contributors
// For license information, please see license.txt


frappe.ui.form.on('GSTIN_fetch', {
	refresh:function(frm){
		let popup = new frappe.ui.Dialog({
			title:"Enter GST Details",
			fields: [
				{
					label : "GST Number",
					fieldname : "gst_number",
					fieldtype : "Data",
					reqd : 1
				}	
			],
			size:'small',
			primary_action_label:"Submit",
			primary_action(values){
				console.log(values)
				frappe.call({
					method:"demo2.demo2.doctype.gstin_fetch.gstin_fetch.callfn", args:{"gst_number":values.gst_number}, 
					callback:function(response) { 
						console.log(response.message)
						console.log(response.message.gst_number)

						frm.set_value("gst_number",response.message.gst_number)
						frm.set_value("business_name",response.message.business_name)
						frm.set_value("address",response.message.address)
						frm.set_value("pincode",response.message.pincode)
						frm.set_value("entity_type",response.message.entity_type)
						frm.set_value("registration_type",response.message.registration_type)
						frm.set_value("department_code",response.message.department_code)
						frm.set_value("nature_of_business",response.message.nature_of_business)
						frm.set_value("registration_date",response.message.registration_date)
					}
	})
		popup.hide();
		}
	})
	popup.show();
	}
});
