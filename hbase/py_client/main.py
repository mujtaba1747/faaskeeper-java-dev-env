import happybase

# Connect to HBase
connection = happybase.Connection('localhost')  # Replace 'localhost' with your HBase server address
connection.open()

# List tables
tables = connection.tables()
print("Tables: ", tables)

# Create a table
table_name = 'my_table_2'
families = {
    'cf1': dict(),  # Column family 'cf1'
}

if table_name.encode() not in tables:
    connection.create_table(table_name, families)
    print(f"Table {table_name} created.")

# Get a table object
table = connection.table(table_name)

# Insert data
table.put(b'row2', {b'cf1:col1': b'value2'})
print("Data inserted.")

# Fetch data
row = table.row(b'row1')
print("Fetched row:", row)

# Scan table
for key, data in table.scan():
    print(key, data)

# Delete table
connection.delete_table(table_name, disable=True)
print(f"Table {table_name} deleted.")

# Close connection
connection.close()
