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