# Forms to use in pages
import forms
# Dictionaries to pass to template context
import dicts
# Models to access our db's tables
import models 

import keystoneclient.v2_0.client as ksclient

def retrieveUser(userName):
    try:
	#right now, this gets username from Django DB.
	#need to change so it queries Keystone
        return models.User.objects.get(name=userName)	#get user object with username matching "userName"
    except: 
        return None 

def retrieve_object(object_type, input_filter, object_name):
    """Retrieve an object from the table object_type,
    narrowed down by the column of input_filter is the
    name of the object.
    """
    try:
        return getattr(models, object_type).objects.get(
                      **{input_filter: object_name})
    except Exception as e: 
        print e
        print "Returning None"
        return None 
