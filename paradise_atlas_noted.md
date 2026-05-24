## Current State (May 18)

- PostgreSQL running
- atlas DB created
- location_types table created but missing proper PK structure (needs fix)
- locations table created
- next step: rebuild location_types with id + link via foreign key


## Current State (May 24)

- Scripts updated to parse csv file and apply data to the location and visit tables.
- Script will erase the current paradise_voyage_raw_import table and create a new one from the csv data
- I attempted to parse the theatre data and add it to the theatre table
- next step: ensure theatre table was correctly imported



