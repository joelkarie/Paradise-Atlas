CREATE VIEW first_view AS
SELECT v.id, l.name AS location_name, t.name AS theatre_name  
FROM visit v
JOIN location l ON l.id = v.location_id
LEFT JOIN theatre t ON t.id = v.theatre_id;