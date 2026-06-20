CREATE VIEW first_view AS
SELECT v.id, l.name AS location_name, t.name AS theatre_name  
FROM visit v
JOIN location l ON l.id = v.location_id
LEFT JOIN theatre t ON t.id = v.theatre_id;

CREATE VIEW housing_distance_view AS
SELECT l.name AS location_name, t.name AS theatre_name, ROUND(v.housing_distance, 2) AS housing_distance
FROM visit v
JOIN location l ON l.id = v.location_id
JOIN theatre t ON t.id = v.theatre_id
WHERE v.housing_distance IS NOT NULL
ORDER BY v.housing_distance DESC;

CREATE VIEW capitol_completion_view AS
SELECT l.name AS capitol_name, cap.year_completed AS year_completed, v.visit_order AS visit_order FROM visit v
JOIN location l on l.id = v.location_id
JOIN capitol cap ON cap.id = v.capitol_id
WHERE v.capitol_id IS NOT NULL
ORDER BY cap.year_completed ASC;

CREATE VIEW visit_order_view AS
SELECT v.visit_order AS visit_number, l.name AS location_name, l.state_province AS state_province, v.date AS date, l.latitude AS latitude, l.longitude AS longitude
FROM visit v 
JOIN location l on l.id = v.location_id
ORDER BY v.visit_order ASC;

CREATE VIEW journey_view AS
SELECT v.visit_number AS visit_number, l.name AS location_name, l.state_province AS state_province, v.date AS date, l.latitude AS latitude, l.longitude AS longitude
FROM visit v 
JOIN location l on l.id = v.location_id
ORDER BY v.date ASC;

CREATE VIEW theatre_view AS
SELECT t.name AS name, l.name AS city, l.state_province AS state_province, v.date AS date, l.latitude AS latitude, l.longitude AS longitude
FROM visit v
JOIN theatre t ON t.id = v.theatre_id
JOIN location l ON l.id = v.location_id
ORDER BY v.visit_order ASC;

CREATE VIEW joel_could_live_view AS
SELECT l.name AS city, l.state_province AS state_province, l.country AS country, l.latitude AS latitude, l.longitude AS longitude
FROM location l 
JOIN location_rating lr ON lr.location_id = l.id
WHERE lr.joel_could_live = True
ORDER BY l.name ASC;

CREATE VIEW capitol_visit_order_view AS
SELECT l.name as city, l.state_province as state_province, l.latitude AS latitude, l.longitude AS longitude, cap.fact AS fact, cap.architect AS architect, cap.architectural_style AS architectural_style, cap.year_completed AS year_completed
FROM visit v
JOIN location l on l.id = v.location_id
JOIN capitol cap ON cap.id = v.capitol_id
ORDER BY v.date ASC;

CREATE VIEW patagonia_visit_view AS
SELECT psv.store_name AS store_name, psv.city AS city, psv.state_province AS state_province, psv.country AS country, psv.latitude AS latitude, psv.longitude AS longitude, psv.visited AS visited
FROM patagonia_store_visit psv;

CREATE VIEW quaker_meeting_house_view AS
SELECT qmh.name AS name, qmh.city AS city, qmh.state_province AS state_province, qmh.latitude AS latitude, qmh.longitude AS longitude
FROM quaker_meeting_house qmh;