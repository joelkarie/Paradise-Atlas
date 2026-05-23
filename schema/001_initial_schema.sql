CREATE TABLE "visit" (
  "id" integer PRIMARY KEY,
  "date" date,
  "original_stop_number" integer,
  "location_id" integer NOT NULL,
  "digs_id" integer,
  "theatre_id" integer,
  "capitol_id" integer,
  "created_at" timestamptz DEFAULT (now()),
  "updated_at" timestamptz DEFAULT (now())
);

CREATE TABLE "location" (
  "id" integer PRIMARY KEY,
  "name" text NOT NULL,
  "alternative_name" text,
  "location_type_id" integer NOT NULL,
  "latitude" numeric(9,6),
  "longitude" numeric(9,6),
  "state_province" text,
  "country" text NOT NULL,
  "created_at" timestamptz DEFAULT (now()),
  "updated_at" timestamptz DEFAULT (now())
);

CREATE TABLE "location_type" (
  "id" integer PRIMARY KEY,
  "name" text UNIQUE NOT NULL
);

CREATE TABLE "national_park_details" (
  "location_id" integer PRIMARY KEY,
  "park_visit_num" integer
);

CREATE TABLE "city_details" (
  "location_id" integer PRIMARY KEY,
  "census_name" text,
  "population" integer,
  "is_city_capital" bool
);

CREATE TABLE "location_rating" (
  "location_id" integer PRIMARY KEY,
  "joel_could_live" bool,
  "michael_could_live" bool,
  "highlight" text,
  "notes" text
);

CREATE TABLE "location_media" (
  "id" integer PRIMARY KEY,
  "location_id" integer NOT NULL,
  "media_type_id" integer NOT NULL,
  "url" text NOT NULL,
  "caption" text
);

CREATE TABLE "media_type" (
  "id" integer PRIMARY KEY,
  "name" text UNIQUE NOT NULL
);

CREATE TABLE "capitol" (
  "id" integer PRIMARY KEY,
  "address" text,
  "latitude" numeric(9,6),
  "longitude" numeric(9,6),
  "capitol_num" integer,
  "highlight" text,
  "created_at" timestamptz DEFAULT (now()),
  "updated_at" timestamptz DEFAULT (now())
);

CREATE TABLE "theatre" (
  "id" integer PRIMARY KEY,
  "name" text NOT NULL,
  "address" text,
  "latitude" numeric(9,6),
  "longitude" numeric(9,6),
  "dresser" text,
  "created_at" timestamptz DEFAULT (now()),
  "updated_at" timestamptz DEFAULT (now())
);

CREATE TABLE "digs" (
  "id" integer PRIMARY KEY,
  "address" text,
  "latitude" numeric(9,6),
  "longitude" numeric(9,6),
  "digs_type_id" integer,
  "company_housing" bool,
  "price_per_night" numeric(10,2),
  "notes" text,
  "created_at" timestamptz DEFAULT (now()),
  "updated_at" timestamptz DEFAULT (now())
);

CREATE TABLE "digs_type" (
  "id" integer PRIMARY KEY,
  "name" text UNIQUE NOT NULL
);

CREATE TABLE "hotel_details" (
  "digs_id" integer PRIMARY KEY,
  "hotel_brand_id" integer
);

CREATE TABLE "hotel_holding_company" (
  "id" integer PRIMARY KEY,
  "name" text UNIQUE NOT NULL
);

CREATE TABLE "hotel_brand" (
  "id" integer PRIMARY KEY,
  "name" text UNIQUE NOT NULL,
  "hotel_holding_company_id" integer
);

ALTER TABLE "visit" ADD FOREIGN KEY ("location_id") REFERENCES "location" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "visit" ADD FOREIGN KEY ("digs_id") REFERENCES "digs" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "visit" ADD FOREIGN KEY ("theatre_id") REFERENCES "theatre" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "visit" ADD FOREIGN KEY ("capitol_id") REFERENCES "capitol" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "location" ADD FOREIGN KEY ("location_type_id") REFERENCES "location_type" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "national_park_details" ADD FOREIGN KEY ("location_id") REFERENCES "location" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "city_details" ADD FOREIGN KEY ("location_id") REFERENCES "location" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "location_rating" ADD FOREIGN KEY ("location_id") REFERENCES "location" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "location_media" ADD FOREIGN KEY ("location_id") REFERENCES "location" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "location_media" ADD FOREIGN KEY ("media_type_id") REFERENCES "media_type" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "digs" ADD FOREIGN KEY ("digs_type_id") REFERENCES "digs_type" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "hotel_details" ADD FOREIGN KEY ("digs_id") REFERENCES "digs" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "hotel_details" ADD FOREIGN KEY ("hotel_brand_id") REFERENCES "hotel_brand" ("id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "hotel_brand" ADD FOREIGN KEY ("hotel_holding_company_id") REFERENCES "hotel_holding_company" ("id") DEFERRABLE INITIALLY IMMEDIATE;
