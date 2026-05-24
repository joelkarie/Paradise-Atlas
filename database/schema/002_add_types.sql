
INSERT INTO location_type (name)
VALUES ('city'), ('national_park'), ('landmark'), ('home')
ON CONFLICT (name) DO NOTHING;

INSERT INTO hotel_holding_company (name)
VALUES ('Marriott'), ('IHG'), ('Sonesta'), ('Hiton'), ('Hyatt'), ('McMenamins'), ('Sonder'), ('Landing')
ON CONFLICT (name) DO NOTHING;

INSERT INTO media_type (name)
VALUES ('manhole_photo')
ON CONFLICT (name) DO NOTHING;

INSERT INTO digs_type (name)
VALUES ('hotel'), ('airbnb'), ('boat'), ('camping'), ('furnished_finder'), ('home'), ('hostel')
ON CONFLICT (name) DO NOTHING;; 
