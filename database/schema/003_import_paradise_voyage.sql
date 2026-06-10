TRUNCATE TABLE paradise_voyage_raw_import;
TRUNCATE TABLE us_capitol_raw_import;

\copy paradise_voyage_raw_import FROM 'flat_files/expanded_paradise_voyage_raw_data.csv' DELIMITER ',' CSV HEADER;
\copy us_capitol_raw_import FROM 'flat_files/us_state_capitols_with_coordinates.csv' DELIMITER ',' CSV HEADER;
\copy canadian_legislative_buildings_import FROM 'flat_files/canadian_legislative_buildings.csv' DELIMITER ',' CSV HEADER;
\copy tour_housing_calculation_import from 'flat_files/tour_housing_calculations.csv' DELIMITER ',' CSV HEADER;
\copy trip_import from 'flat_files/trip_dates.csv' DELIMITER ',' CSV HEADER;
\copy patagonia_store_visit_import from 'flat_files/patagonia_visit_data.csv' DELIMITER ',' CSV HEADER;
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
SELECT DISTINCT ON (l.id)
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
SELECT DISTINCT ON (l.id)
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
SELECT DISTINCT ON (d.id)
    d.id,
    hb.id
FROM paradise_voyage_raw_import r 
JOIN digs d
    ON d.address = r."Digs Address"
JOIN hotel_brand hb
    ON hb.name = r."Hotel Brand";


INSERT INTO capitol (
    name,
    address,
    latitude,
    longitude,
    capitol_num,
    year_completed,
    architect,
    architectural_style,
    size_sq_ft,
    dome_height,
    fact,
    country
)
SELECT
    c."State",
    NULLIF(NULLIF(NULLIF(c."Capitol Address", '-'), '~'), '')::text,
    NULLIF(NULLIF(c."Latitude", '-'), '')::numeric,
    NULLIF(NULLIF(c."Longitude", '-'), '')::numeric,
    NULLIF(NULLIF(r."Capitol Num", '-'), '')::numeric,
    c."Year Completed",
    c."Architect",
    c."Architectural Style",
    NULLIF(NULLIF(c."Approximate Size (sq ft)", '-'), '')::numeric,
    NULLIF(NULLIF(NULLIF(c."Dome Height", '-'), '~'), '')::text,
    c."Trivia Fact",
    'USA'
FROM us_capitol_raw_import c
JOIN LATERAL (
    SELECT r."Capitol Num"
    FROM paradise_voyage_raw_import r
    WHERE r."State/Province" = c."State"
      AND r."Capitol" = 'TRUE'
    LIMIT 1
) r ON TRUE;

INSERT INTO capitol (
    name,
    address,
    latitude,
    longitude,
    capitol_num,
    year_completed,
    architect,
    architectural_style,
    size_sq_ft,
    dome_height,
    fact, 
    country
)
SELECT
    c."Province/Territory",
    NULLIF(NULLIF(NULLIF(c."Address", '-'), '~'), '')::text,
    NULLIF(NULLIF(c."Latitude", '-'), '')::numeric,
    NULLIF(NULLIF(c."Longitude", '-'), '')::numeric,
    NULLIF(NULLIF(r."Capitol Num", '-'), '')::numeric,
    c."Year Completed",
    c."Architect",
    c."Architectural Style",
    NULLIF(
    REPLACE(NULLIF(c."Approximate Size (sq ft)", ''), ',', ''),
    ''
)::numeric,
    NULLIF(NULLIF(NULLIF(c."Height / Dome Height", '-'), '~'), '')::text,
    c."Trivia Fact",
    'Canada'
FROM canadian_legislative_buildings_import c
JOIN LATERAL (
    SELECT r."Capitol Num"
    FROM paradise_voyage_raw_import r
    WHERE r."State/Province" = c."Province/Territory"
      AND r."Capitol" = 'TRUE'
    LIMIT 1
) r ON TRUE;

INSERT INTO patagonia_store_visit (
    store_name,
    city,
    state_province,
    country,
    address,
    postal_code,
    latitude,
    longitude,
    visited
)
SELECT
    "name",
    "city",
    "state_province",
    "country",
    "address",
    "postal_code",
    NULLIF(NULLIF("latitude", '-'), '')::numeric,
    NULLIF(NULLIF("longitude", '-'), '')::numeric,
    NULLIF(NULLIF("visited", '-'), '')::boolean
FROM patagonia_store_visit_import;

INSERT INTO visit (
    date,
    visit_number,
    visit_order,
    original_stop_number,
    location_id, 
    theatre_id, 
    digs_id,
    housing_distance,
    capitol_id
)
SELECT
    NULLIF(NULLIF(NULLIF(r."Visit Date", '-'), '~'), '')::date,
    NULLIF(NULLIF(NULLIF(r."Visit Number", '-'), '~'), '')::integer,
    NULLIF(NULLIF(NULLIF(r."Visit Order", '-'),'~'), '')::integer,
    NULLIF(NULLIF(NULLIF(r."Original Stop Number", '-'), '~'), '')::integer,
    l.id,
    t.id,
    d.id,
    NULLIF(TRIM(NULLIF(NULLIF(r."Housing Dist", '-'), '~')), '')::float,
    cap.id
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
LEFT JOIN city_details cd
    ON cd.location_id = l.id
LEFT JOIN capitol cap
    ON cap.name = l.state_province
   AND cap.country = l.country
   AND cd.is_city_capital = TRUE
ON CONFLICT (date, location_id) DO NOTHING;

INSERT INTO housing_calculations (
    digs_id,
    total_paid_personal,
    total_company_paid,
    total_days_stayed,
    daily_cost,
    daily_buyout,
    daily_housing_buyout,
    other_stay,
    total_spent,
    weeks,
    combined_weekly_buyout,
    housing_buyout,
    housing_savings
)
SELECT
    v.digs_id,
    NULLIF(NULLIF(NULLIF(th."Total Digs Paid", '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Company Housing Days",  '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Total Stayed",  '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Daily Cost",  '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Daily Buyout", '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Daily Housing Buyout", '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Other Stay", '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Total Spent", '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Weeks", '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Total Buyout", '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Housing Buyout", '-'), '~'), '')::numeric,
    NULLIF(NULLIF(NULLIF(th."Housing Savings", '-'), '~'), '')::numeric
FROM tour_housing_calculation_import th
JOIN location l on l.name = th."City" AND l.state_province = th."State/Province"
JOIN visit v ON v.location_id = l.id;

INSERT INTO trip (name, start_date, end_date, description)
SELECT
    "Trip Name",
    NULLIF(NULLIF(NULLIF("Start Date", '-'), '~'), '')::date,
    NULLIF(NULLIF(NULLIF("Finish Date", '-'), '~'), '')::date,
    NULLIF(NULLIF(NULLIF("Order", '-'), '~'), '')::integer
FROM trip_import;
-- ON CONFLICT (name, start_date, end_date) DO NOTHING;