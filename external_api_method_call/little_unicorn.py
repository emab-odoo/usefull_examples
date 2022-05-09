import xmlrpc.client
import datetime
import pytz
url = "http://localhost:8069"
db = "test"
username = 'admin'
password = "admin"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})

records = models.execute_kw(db, uid, password, 'sale.order', 'example_method', [[]], {'test': 5000})

print(records)