CREATE VIEW first_view AS
SELECT v.id, l.name AS location_name, t.name AS theatre_name  
FROM visit v
JOIN location l ON l.id = v.location_id
LEFT JOIN theatre t ON t.id = v.theatre_id;

CREATE VIEW housing_distance_view AS
SELECT l.name AS "Location Name", t.name AS "Venue", ROUND(v.housing_distance, 2) AS "Distance To Housing"
FROM visit v
JOIN location l ON l.id = v.location_id
JOIN theatre t ON t.id = v.theatre_id
WHERE v.housing_distance IS NOT NULL
ORDER BY v.housing_distance DESC;

CREATE VIEW capitol_completion_view AS
SELECT l.name AS "Capital", cap.year_completed AS "Completion", v.visit_order AS "Visit Num" FROM visit v
JOIN location l on l.id = v.location_id
JOIN capitol cap ON cap.id = v.capitol_id
WHERE v.capitol_id IS NOT NULL
ORDER BY cap.year_completed ASC;

CREATE VIEW visit_order_view AS
SELECT v.visit_order AS "Visit Number", l.name AS "Location", l.state_province AS "State/Province", v.date AS "Date", l.latitude AS "Latitude", l.longitude AS "Longitude"
FROM visit v 
JOIN location l on l.id = v.location_id
ORDER BY v.visit_order ASC;

CREATE VIEW theatre_view AS
SELECT t.name AS "Venue", l.name AS "City", l.state_province AS "State/Province", v.date AS "Date", l.latitude AS "Latitude", l.longitude AS "Longitude"
FROM visit v
JOIN theatre t ON t.id = v.theatre_id
JOIN location l ON l.id = v.location_id
ORDER BY v.visit_order ASC;

CREATE VIEW joel_could_live_view AS
SELECT l.name AS "City", l.state_province AS "State/Province", l.country AS "Country"
FROM location l 
JOIN location_rating lr ON lr.location_id = l.id
WHERE lr.joel_could_live = True
ORDER BY l.name ASC;

CREATE VIEW capitol_visit_order_view AS
SELECT l.name as "City", l.state_province as "State?Province", l.latitude AS "Latitude", l.longitude AS "Longitude"
FROM visit v
JOIN location l on l.id = v.location_id
JOIN capitol cap ON cap.id = v.capitol_id
ORDER BY v.date ASC;