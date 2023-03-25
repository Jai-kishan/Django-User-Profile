import django
import os
import sys
import pandas as pd

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DFSL.settings')
django.setup()

from w3school_sql.models import *

# def customer_records(data):
#     res = Customer.objects.create(CustomerName=data.get("CustomerName"),
#                                   ContactName=data.get("ContactName"),
#                                   Address=data.get("Address"),
#                                   City=data.get("City"),
#                                   PostalCode=data.get("PostalCode"),
#                                   Country=data.get("Country")
#                                   )
#     print(res)


# def categories_records(data):
#     res = Category.objects.create(
#         CategoryID = data.get('CategoryID'),
#         CategoryName = data.get('CategoryName'),
#         Description = data.get('Description').replace("_",",")
#     )

# df = pd.read_csv('w3school_sql/Customers.csv')
# df = df.iloc[1:]
# df.apply(customer_records, axis=1)


