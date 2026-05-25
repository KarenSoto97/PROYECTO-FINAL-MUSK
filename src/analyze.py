import pandas as pd
import json

from client import Client
from sale import Sale
from client_collection import ClientCollection
from sales_collection import SalesCollection

# Read files:

path_client = r"C:\Users\prisc\OneDrive\Python_new\1. Python\Módulo 7_2\PROYECTO-FINAL-MUSK\data\clients.json"
path_sales = r"C:\Users\prisc\OneDrive\Python_new\1. Python\Módulo 7_2\PROYECTO-FINAL-MUSK\data\sales.csv"

with open(path_client, 'r', encoding='utf-8') as data:
    data_clients = json.load(data)

data_sales_df = pd.read_csv(path_sales)
data_sales_dict = data_sales_df.to_dict(orient="records")

# Client list:

client_list = []

for client in data_clients:

    client_id = client.get('client_id')
    name = client.get('name')
    country = client.get('country')
    signup_date = client.get('signup_date')

    new_client = Client(client_id=client_id, name=name, country=country, signup_date=signup_date)
    client_list.append(new_client)

client_collection = ClientCollection(client_list=client_list)

# Sales list:

sales_list = []

for sale in data_sales_dict:

    sale_id = sale.get('sale_id')
    client_id = sale.get('client_id')
    product = sale.get('product')
    category = sale.get('category')
    amount = sale.get('amount')
    date = sale.get('date')

    new_sale = Sale(sale_id=sale_id, client_id=client_id, product=product, category=category, amount=amount, date=date)
    sales_list.append(new_sale)

sales_collection = SalesCollection(sales_list=sales_list)

# 1. Number of clients

total_num_clients = len(client_list)

# 2. Number of sales

total_num_sales = data_sales_df.shape[0]

# 3. Total income by client:

total_income_by_client = {}

for client in client_list:
    client_id = client.client_id
    total_income = sales_collection.total_amount_by_client(client_id=client_id)
    total_income_by_client[client_id] = total_income

# 4. Number of sales by client

num_sales_by_client = {}

for client in client_list:
    client_id = client.client_id
    num_sales = len(sales_collection.sales_by_client(client_id=client_id))
    num_sales_by_client[client_id] = num_sales

# 5. Average sale by client

average_sale_by_client = {}

for client in client_list:
    client_id = client.client_id
    mean_sales = sales_collection.average_sale_by_client(client_id=client_id)
    average_sale_by_client[client_id] = mean_sales

# 6. Highest spending client by country

countries = {c.country for c in client_list}
best_client_by_country = {}

for country in countries:

    best_amount = 0
    best_client_id = 0

    country_clients = client_collection.clients_by_country(country=country)
   
    for client_obj in country_clients:
        client_id = client_obj.client_id
        current_amount = sales_collection.total_amount_by_client(client_id)

        if current_amount > best_amount:
            best_amount = current_amount
            best_client_id = client_id
    
    best_client_by_country[country] = (best_client_id, best_amount)


