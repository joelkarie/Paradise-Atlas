import pandas as pd
from sqlite3 import connect


# Convert data from Google Sheets csv to dataframe.
URL = "https://docs.google.com/spreadsheets/d/1In0n2i5ILXrA8HmhlHQVQIGQTzGU5Ce-Y2LgWp_R0Y8/export?format=csv"
original_df = pd.read_csv(URL, true_values=["TRUE"], false_values=["FALSE"])

# Work with a copy of the dataframe.
df =original_df.copy()

columns = df.keys()

print(columns)

# Create database connection
# brew services start postgresqlbrew services start postgresql
