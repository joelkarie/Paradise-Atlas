import pandas as pd
from pathlib import Path

"""
Script uses a csv to check if there is a corresponding image in the local /locations folder.
"""

file = 'location_id_name_has_image.csv' # CSV has been manually created from DBeaver query

# Convert CSV to dataframe.
df = pd.read_csv(file)

for i, row in df.iterrows():
    name = row['name']
    has_image = row['has_image']

    url1 = Path(f"../frontend/images/locations/{id}_location.webp")

    if url1.exists():
        # print(f"{name} has an image file")
        df.at[i, 'has_image'] = True
    else:
        print(f"{name} has no image file")

df.to_csv("updated_update_has_image.csv")