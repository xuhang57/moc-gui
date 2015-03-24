## SAMPLE
sample_buttons = [{'name': 'NAME', 'type': 'BUTTON-TYPE', 'action': '/URL/', 'class': 'btn-primary'},]

sample_form_data = {'name': 'TITLE', 'action': '/URL', 'method': 'post', 'button_list': sample_buttons} 

sample_modal = {'id': 'createUser', 'action': '/register', 'method': 'post', 'title': 'Register User'} 

## FRONT PAGE
login_buttons = [{'name': 'submit', 'type': 'submit', 'action': '/login/', 'class': 'btn-primary'}, 
                 {'name': 'sign-up', 'type': 'modal', 'data_target': '#createUser', 'class': 'btn-success'}] 

login_data = {'name': 'MassOpenCloud Login', 'action': '/login', 'method': 'post', 'button_list': login_buttons} 

reg_modal = {'id': 'createUser', 'action': '/register', 'method': 'post', 'title': 'Register User'} 


# CLOUDS PAGE
test_vm_list_1 = [{'name': 'hadoop master', 'state': '=)', 'provider': 'HU-prod', 'image': 'centOS 7.jpg'},
                {'name': 'hadoop slave 1', 'state': '=)', 'provider': 'BU-prod', 'image': 'centOS 7'},
                {'name': 'hadoop slave 2', 'state': '=)', 'provider': 'NE-prod', 'image': 'centOS 7'},
                {'name': 'hadoop slave 2', 'state': 'build', 'provider': 'UMASS-prod', 'image': 'centOS 7'},
                {'name': 'hadoop slave 3', 'state': 'off', 'provider': 'HU-dev', 'image': 'centOS 7'},
                {'name': 'bad machine', 'state': '=(', 'provider': 'MIT-dev', 'image': 'Windows 8'}]

test_vm_list_2 = [{'name': 'web server', 'state': '=)', 'provider': 'HU-prod', 'image': 'Ubuntu 14.10'},
                {'name': 'database', 'state': 'build', 'provider': 'HU-dev', 'image': 'Suse'},]

test_project_list = [{'name': 'big_data', 'vm_list': test_vm_list_1}, 
                     {'name': 'webservers', 'vm_list': test_vm_list_2}]

# MARKET PAGE
test_service_list = [{'name': 'Hadoop', 'state': '=)', 'provider': 'HU-prod', 'image': 'centOS 7'},
                ]
                
test_market_list = [{'name': 'Service','market_choice_list': test_service_list}, 
                     {'name': 'Hive and Pig'}]

test_market_list = [{'name':'Dell','provider':'Dell','description':'Dell Compute', 'version':'3.1.4', 'availability':'Yes', 'type':'Compute', 'image':'centOS 7'},
                    {'name':'HP','provider':'HP','description':'HP Compute', 'version':'3.1.4', 'availability':'Yes', 'type':'Compute', 'image':'centOS 7'},
                    {'name':'Intel','provider':'Intel','description':'Intel Compute', 'version':'3.1.4', 'availability':'Yes', 'type':'Compute', 'image':'centOS 7'},
                    {'name':'EMC','provider':'EMC','description':'EMC Storage', 'version':'3.1.4', 'availability':'Yes', 'type':'Storage', 'image':'centOS 7'},
                    {'name':'NetApp','provider':'NetApp','description':'NetApp Storage', 'version':'3.1.4', 'availability':'Yes', 'type':'Storage', 'image':'centOS 7'},
                    {'name':'Brocade','provider':'Brocade','description':'Brocade Networking', 'version':'3.1.4', 'availability':'Yes', 'type':'Network', 'image':'centOS 7'},
                    {'name':'Juniper','provider':'Juniper','description':'Juniper Networking', 'version':'3.1.4', 'availability':'Yes', 'type':'Network', 'image':'centOS 7'},
                    {'name':'Cisco','provider':'Cisco','description':'Cisco Networking', 'version':'3.1.4', 'availability':'Yes', 'type':'Network', 'image':'centOS 7'}]
