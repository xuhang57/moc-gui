from os import environ as env
import novaclient.v1_1.client as nvclient
import glanceclient.v2.client as glclient
import keystoneclient.v2_0.client as ksclient


def loginUser(username, password,request):
        """
	Create keystone client for user; called on login
	"""
	print 'lucas-test-auth-loginUser'
	
        keystone = ksclient.Client(
	        auth_url = 'http://140.247.152.207:5000/v2.0',
		username = username,
       		password = password)
    	print 'lucas-test-auth-loginUser-succesfully'
	return keystone

def loginTenant(username, password, tenantName,request):
        """
	Create keystone, nova, and glance clients for tenant; on tenant selection
	"""
	print 'lucas-test-auth-loginTenant'
        keystone = ksclient.Client(
	        auth_url = 'http://140.247.152.207:5000/v2.0',
		username = username,
                password = password,
                tenant_name = tenantName)
        print 'lucas-test-auth-loginTenant-succesfully'
	nova = nvclient.Client(
	        auth_url = 'http://140.247.152.207:5000/v2.0',
		username = username,
                api_key = password,
		project_id = tenantName)
	glance_endpoint = keystone.service_catalog.url_for(service_type='image')
        glance = glclient.Client(
                glance_endpoint,
                token = keystone.auth_token)
	return keystone, nova, glance


##### OUTDATED SECTION - USEFUL FOR TESTING
# admin keystone auth
#keystone = ksclient.Client(token='admin', endpoint='http://10.0.2.15:35357/v2.0')

#keystoneImages = ksclient.Client(auth_url=env['OS_AUTH_URL'],
#username=env['OS_USERNAME'],
#password=env['OS_PASSWORD'],
#tenant_name=env['OS_TENANT_NAME'],
#region_name=env['OS_REGION_NAME'])

#glance_endpoint = keystoneImages.service_catalog.url_for(service_type='image')
#glance = glclient.Client(glance_endpoint, token=keystoneImages.auth_token)

#nova = nvclient.Client(auth_url=env['OS_AUTH_URL'],
#username=env['OS_USERNAME'],
#api_key=env['OS_PASSWORD'],
#project_id=env['OS_TENANT_NAME'],
#region_name=env['OS_REGION_NAME'])
#####


