TRUNCATE TABLE paradise_voyage_raw_import;

\copy paradise_voyage_raw_import FROM 'paradise_voyage_raw_data.csv' DELIMITER ',' CSV HEADER;

-- psql -d atlas_paradiso -f 003_import_paradise_voyage.sql

INSERT INTO location (
    name,
    alternative_name,
    location_type_id,
    latitude,
    longitude,
    state_province,
    country, 
    census_name
)
SELECT DISTINCT
    "City",
    NULL,
    CASE
        WHEN "Location Type" ILIKE 'city' THEN 1
        WHEN "Location Type" ILIKE 'national park' THEN 2
        WHEN "Location Type" ILIKE 'landmark' THEN 3
        ELSE 1
    END,
    NULLIF(NULLIF(NULLIF("Latitude", '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF("Longitude", '-'), '~'), '')::numeric,
    "State/Province",
    "Country",
    "Census Name"
FROM paradise_voyage_raw_import
ON CONFLICT (name, state_province, country)
DO NOTHING;

INSERT INTO location_rating (location_id, joel_could_live, michael_could_live, highlight)
SELECT
    l.id,
    NULLIF(NULLIF(r."Joel Could Live", '-'), '')::boolean,
    NULLIF(NULLIF(r."Michael Could Live", '-'), '')::boolean,
    NULLIF(NULLIF(r."Highlight", '-'), '')::text
FROM paradise_voyage_raw_import r 
JOIN location l
    ON l.name = r."City"
   AND l.state_province = r."State/Province"
   AND l.country = r."Country";

INSERT INTO city_details (location_id, population, is_city_capital)
SELECT
    l.id,
    NULLIF(
    REPLACE(NULLIF(NULLIF(r."Population", '-'), ''), ',', ''),'')::integer,
    NULLIF(NULLIF(r."Capitol", '-'), '')::boolean
FROM paradise_voyage_raw_import r 
JOIN location l
    ON l.name = r."City"
   AND l.state_province = r."State/Province"
   AND l.country = r."Country";

INSERT INTO theatre (name, address, latitude, longitude)
SELECT DISTINCT
    "Theatre",
    "Theatre Address",
    NULLIF(NULLIF("Theatre Lat", '-'), '')::numeric,
    NULLIF(NULLIF("Theatre Lon", '-'), '')::numeric
FROM paradise_voyage_raw_import
WHERE "Theatre" IS NOT NULL
  AND "Theatre" <> ''
ON CONFLICT (name, address) DO NOTHING;

INSERT INTO digs (address, latitude, longitude, digs_type_id, company_housing)
SELECT DISTINCT
    r."Digs Address",
    NULLIF(NULLIF(r."Digs Lat", '-'), '')::numeric,
    NULLIF(NULLIF(r."Digs Lon", '-'), '')::numeric,
    dt.id,
    CASE
        WHEN r."Company Housing" ILIKE 'TRUE' THEN TRUE
        ELSE FALSE
    END
FROM paradise_voyage_raw_import r
LEFT JOIN digs_type dt
    ON LOWER(dt.name) = LOWER(r."Digs")
WHERE r."Digs Address" IS NOT NULL
    AND r."Digs Address" <> ''
ON CONFLICT (address) DO NOTHING;

INSERT INTO hotel_brand (name, hotel_holding_company_id)
SELECT DISTINCT
    r."Hotel Brand",
    hc.id
FROM paradise_voyage_raw_import r
JOIN hotel_holding_company hc
    ON hc.name = r."Hotel Holding";

INSERT INTO hotel_details (digs_id, hotel_brand_id)
SELECT
    d.id,
    hb.id
FROM paradise_voyage_raw_import r 
JOIN digs d
    ON d.address = r."Digs Address"
JOIN hotel_brand hb
    ON hb.name = r."Hotel Brand";

INSERT INTO visit (
    date,
    visit_order,
    original_stop_number,
    location_id, 
    theatre_id, 
    digs_id,
    housing_distance
)
SELECT
    NULLIF(NULLIF(NULLIF(r."Visit Date", '-'), '~'), '')::date,
    NULLIF(NULLIF(NULLIF(r."Visit Order", '-'),'~'), '')::integer,
    NULLIF(NULLIF(NULLIF(r."Original  Stop Number", '-'), '~'), '')::integer,
    l.id,
    t.id,
    d.id,
    NULLIF(NULLIF(NULLIF(r."Housing Dist", '-'), '~'), '')::float
FROM paradise_voyage_raw_import r
JOIN location l
    ON l.name = r."City"
   AND l.state_province = r."State/Province"
   AND l.country = r."Country"
LEFT JOIN theatre t
    ON t.name = r."Theatre"
   AND t.address = r."Theatre Address"
LEFT JOIN digs d
    ON d.address = r."Digs Address"
ON CONFLICT (date, location_id) DO NOTHING;