import pandas as pd
from sqlalchemy import create_engine
from sqlite3 import connect


# Convert data from Google Sheets csv to dataframe.
URL = "https://docs.google.com/spreadsheets/d/1In0n2i5ILXrA8HmhlHQVQIGQTzGU5Ce-Y2LgWp_R0Y8/export?format=csv"
original_df = pd.read_csv(URL, true_values=["TRUE"], false_values=["FALSE"])

# Work with a copy of the dataframe.
df =original_df.copy()

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("/", "_")
)
columns = df.keys()

print(columns)

types = df["location_type"].dropna().unique()
print(types)

# # Create database connection
# # Connect to PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://localhost/atlas"
)

df.to_sql(
    "locations",
    engine,
    if_exists="replace",
    index=False
)

# psql atlas
types_df = pd.DataFrame(types, columns=["name"])
types_df.to_sql("location_types", engine, if_exists="append", index=False)

type_map = pd.read_sql("SELECT * FROM location_types", engine)

df = df.merge(
    type_map,
    left_on="location_type",
    right_on="name",
    how="left"
)

df = df.rename(columns={"id": "location_type_id"})

df = df.drop(columns=["location_type", "name"])
print("Joel: end of script")
# brew services start postgresqlbrew services start postgresql