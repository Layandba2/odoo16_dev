import csv
import xmlrpc.client

url = 'http://localhost:8069'
db = 'odoo16_demo_data'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# authentication
uid = common.authenticate(db, username, password, {})
if uid:
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    with open('data.csv', 'r') as orderdata:
        csvreader = csv.reader(orderdata)
        fields = next(csvreader)

        for row in csvreader:
            print(row)
            vals = {
                'employee_id': row[0],
                'order_date_time': row[1],
                'supplier_id': row[2]
            }
            created_id = models.execute_kw(db, uid, password, 'meal.order', 'create', [vals])
else:
    print("Failed")