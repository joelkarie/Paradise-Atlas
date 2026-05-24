-- You will now be able to run:

-- psql -d atlas_paradiso -f import_paradise.sql

-- and it will:

-- wipe old data
-- reload CSV
-- clean everything
-- rebuild your final table


TRUNCATE TABLE paradise_voyage_raw_import;
TRUNCATE TABLE paradise_voyage;

\copy paradise_voyage_raw_import
FROM 'paradise_voyage_raw_data.csv'
DELIMITER ','
CSV HEADER;

INSERT INTO paradise_voyage (
    visit_order, city, state_province, country,
    latitude, longitude, year_visited, visit_date,
    location_type, census_name, capitol, capitol_num,
    number_of_visits, tour_stop, theatre, theatre_address,
    theatre_lat, theatre_lon, company_housing, digs,
    hotel_brand, digs_address, digs_lat, digs_lon,
    housing_dist, num_hotels, joel_could_live, michael_could_live,
    highlight, original_stop_number, aka, manhole, population
)
SELECT
    NULLIF(NULLIF(NULLIF("Visit Order", '-'), '~'), '')::INTEGER,
    "City",
    "State/Province",
    "Country",
    NULLIF(NULLIF(NULLIF("Latitude", '-'), '~'), '')::DOUBLE PRECISION,
    NULLIF(NULLIF(NULLIF("Longitude", '-'), '~'), '')::DOUBLE PRECISION,
    NULLIF(NULLIF(NULLIF("Year Visited", '-'), '~'), '')::INTEGER,
    NULLIF(NULLIF(NULLIF("Visit Date", '-'), '~'), '')::DATE,
    "Location Type",
    "Census Name",
    NULLIF(NULLIF(NULLIF("Capitol", '-'), '~'), '')::BOOLEAN,
    NULLIF(NULLIF(NULLIF("Capitol Num", '-'), '~'), '')::INTEGER,
    NULLIF(NULLIF(NULLIF("Number of Visits", '-'), '~'), '')::INTEGER,
    NULLIF(NULLIF(NULLIF("Tour Stop", '-'), '~'), '')::BOOLEAN,
    "Theatre",
    "Theatre Address",
    NULLIF(NULLIF(NULLIF("Theatre Lat", '-'), '~'), '')::DOUBLE PRECISION,
    NULLIF(NULLIF(NULLIF("Theatre Lon", '-'), '~'), '')::DOUBLE PRECISION,
    NULLIF(NULLIF(NULLIF("Company Housing", '-'), '~'), '')::BOOLEAN,
    "Digs",
    "Hotel Brand",
    "Digs Address",
    NULLIF(NULLIF(NULLIF("Digs Lat", '-'), '~'), '')::DOUBLE PRECISION,
    NULLIF(NULLIF(NULLIF("Digs Lon", '-'), '~'), '')::DOUBLE PRECISION,
    NULLIF(NULLIF(NULLIF("Housing Dist", '-'), '~'), '')::DOUBLE PRECISION,
    NULLIF(NULLIF(NULLIF("Num Hotels", '-'), '~'), '')::INTEGER,
    NULLIF(REPLACE(NULLIF(NULLIF("Population", '-'), '~'), ',', ''), '')::INTEGER
FROM paradise_voyage_raw_import;