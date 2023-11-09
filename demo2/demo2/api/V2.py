import frappe
import demo2.demo2.api.v2.fetch_gst as post_gstdata


class V1():
    def __init__(self):
        self.methods = {
            'post_gstdata':['gst_fetch'],

             }
        
    def class_map(self, kwargs):    
        entity = kwargs.get('entity')
        method = kwargs.get('method')
        if self.methods.get(entity):
            if method in self.methods.get(entity):
                function = f"{kwargs.get('entity')}.{kwargs.get('method')}({kwargs})"
                return eval(function)
            else:
                return error_response("Method Not Found!")
        else:
            return error_response("Entity Not Found!")