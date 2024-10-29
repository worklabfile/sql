#пока что есть ошибки с подключением в google cloud

# from google.cloud import bigquery

# client = bigquery.Client()

# dataset_ref = client.dataset('hacker_news',project = 'bigquery-public-data')

# dataset = client.get_dataset(dataset_ref)

# tables = list(client.list_tables(dataset))

# for table in tables:
#     print(table.tableid)

# table_ref = dataset_ref.table('full')

# table = client.get_table(table_ref)

# print(table.schema)

# client.list_rows(table,selected_fields=table.schema[:1], max_results=5).to_dataframe()

from google.cloud import bigquery

# Create a "Client" object
client = bigquery.Client()

# Construct a reference to the "chicago_crime" dataset
dataset_ref = client.dataset("chicago_crime", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))

print(len(tables))

query = """
        SELECT city
        FROM `bigquery-public-data.openaq.global_air_quality`
        WHERE country = 'US'
        """




