import requests
import pandas as pd
from sqlalchemy import create_engine

# 1. Consume an API (using a public placeholder API)
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()
print(data)
exit()
# 2. Convert to DataFrame
df = pd.DataFrame(data)

# 3. Add a New Column
# Adding a static 'status' column for all rows
df['status'] = 'active'

# 4. Add a New Row
# We create a dictionary with matching keys and append it
new_row = {'id': 11,
           'name': 'John Doe',
           'username': 'jdoe',
           'email': 'jdoe@example.com',
           'status': 'pending'}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# 5. Print Total Rows and Columns
rows, cols = df.shape
print(f"Total Rows: {rows}")
print(f"Total Columns: {cols}")

# 6. Insert into an SQL Database (SQLite file)
# 'sqlite:///my_data.db' creates a local database file in your directory
engine = create_engine('sqlite:///data_warehouse.db')
df.to_sql('users_table', con=engine, if_exists='replace', index=False)

print("Data successfully exported to SQL.")
