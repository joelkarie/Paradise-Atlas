Table visit {
  id integer [pk]
  date date
  original_stop_number integer
  location_id integer [not null]
  digs_id integer
  theatre_id integer
  capitol_id integer
  created_at timestamptz [default: `now()`]
  updated_at timestamptz [default: `now()`]
}

Table location {
  id integer [pk]
  name text
  alternative_name text
  location_type_id integer [not null]
  latitude numeric(9,6)
  longitude numeric(9,6)
  state_province text
  country text [not null]
  created_at timestamptz [default: `now()`]
  updated_at timestamptz [default: `now()`]
}
Table location_type {
  id integer [pk]
  name text [not null]
}
Table national_park_details {
  location_id integer [pk]
  park_visit_num integer
}
Table city_details {
  location_id integer [pk]
  census_name text
  population integer
  capital bool
}
Table location_rating {
  location_id integer [pk]
  joel_could_live bool
  michael_could_live bool
  highlight text
  notes text
}
Table location_media {
  id integer [pk]
  location_id integer [not null]
  media_type_id integer [not null]
  url text [not null]
  caption text
}
Table media_type {
  id integer [pk]
  name text [not null]
}
Table capitol {
  id integer [pk]
  address text
  latitude numeric(9,6)
  longitude numeric(9,6)
  capitol_num integer
  highlight text
  created_at timestamptz [default: `now()`]
  updated_at timestamptz [default: `now()`]
}
Table theatre {
  id integer [pk]
  name text
  address text
  latitude numeric(9,6)
  longitude numeric(9,6)
  dresser text
  created_at timestamptz [default: `now()`]
  updated_at timestamptz [default: `now()`]
}
Table digs {
  id integer [pk]
  address text
  latitude numeric(9,6)
  longitude numeric(9,6)
  digs_type_id integer
  company_housing bool
  price_per_night float
  notes text
  created_at timestamptz [default: `now()`]
  updated_at timestamptz [default: `now()`]
}
Table digs_type {
  id integer [pk]
  name text
}
Table hotel_details {
  digs_id integer [pk]
  hotel_brand_id integer
}
Table hotel_holding_company {
  id integer [pk]
  name text
}
Table hotel_brand {
  id integer [pk]
  name text
  hotel_holding_company_id integer
}

Ref: visit.location_id > location.id
Ref: visit.digs_id > digs.id
Ref: visit.theatre_id > theatre.id
Ref: visit.capitol_id > capitol.id
Ref: location.location_type_id > location_type.id
Ref: national_park_details.location_id > location.id
Ref: city_details.location_id > location.id
Ref: location_rating.location_id > location.id
Ref: location_media.location_id > location.id
Ref: location_media.media_type_id > media_type.id
Ref: digs.digs_type_id > digs_type.id
Ref: hotel_details.digs_id > digs.id
Ref: hotel_details.hotel_brand_id > hotel_brand.id
Ref: hotel_brand.hotel_holding_company_id > hotel_holding_company.id

