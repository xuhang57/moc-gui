rm db.sqlite3
python manage.py syncdb
python manage.py loaddata service_list.json
