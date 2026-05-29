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

## Current State (May 27)

- Parsed digs added (manually) to tables and joined to the visits table. 
- first_view was created that allows me to see the theatres associated with visits/locations.
- next step: correclty import digs to save brands and holding companies. correct order of capitols

## Current State (May 28)

- Enriched the digs table
- Updated csv info
- next step: fix hotel holding/brand join. Add some custom views.

## Current State (May 29)

- Corrected hotel tables.

- next step: correct 'Original Stop Number"