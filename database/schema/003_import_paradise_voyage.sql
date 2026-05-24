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
    country
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
    "Country"
FROM paradise_voyage_raw_import
ON CONFLICT (name, state_province, country)
DO NOTHING;

INSERT INTO visit (
    date,
    original_stop_number,
    location_id
)
SELECT
    NULLIF(NULLIF(NULLIF("Visit Date", '-'), '~'), '')::date,
    NULLIF(NULLIF(NULLIF("Original  Stop Number", '-'), '~'), '')::integer,
    l.id
FROM paradise_voyage_raw_import r
JOIN location l
    ON l.name = r."City"
   AND l.state_province = r."State/Province"
   AND l.country = r."Country"
LEFT JOIN theatre t
    ON t.name = r."Theatre"
   AND t.address = r."Theatre Address"
ON CONFLICT (date, location_id) DO NOTHING;

INSERT INTO theatre (name, address, latitude, longitude)
SELECT DISTINCT
    "Theatre",
    "Theatre Address",
    NULLIF(NULLIF("Theatre Lat", '-'), '')::numeric,
    NULLIF(NULLIF("Theatre Lon", '-'), '')::numeric
FROM paradise_voyage_raw_import
WHERE "Theatre" IS NOT NULL
  AND "Theatre" <> '';