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
- capitol table was added with correct inserts.
- housing_distance_view added
- next step: correct 'Original Stop Number"

## Current State (May 30)

- Canadian legislative building csv imported and added to capitol table
- capitol table joined with visit table
- excel sheet containing housing costs for 2026 & 20205 created saved in Mac::/Documents/Rafiki
- capitol_completion_view added to views
- next step: correct 'Original Stop Number', research data visualization (DBeaver?)

## Current State (June 4)

- Updated visit csv with all stop dates.
- Added tour housing calculation csv and table.
- next step: create tour housing view. add all stops to visit csv (this will take some time)

## Current State (June 6)

- Add additional housing calculations
- Add route handlers
- next step: Patagonia table.

## Current State (June 6)

- Add updated visit information csv
- Move csv's into a dedicated folder
- Add updated csv data to tables
- Add journey_view 
- Add trip data and tables
- Add patagonia data and tables
- Add routers and services
- next step: Build maps with routers/services

## Current State (June 18)

- Api Created
- Maps are updating using Javascript
- Maps have custom icons
- next step: create journey data