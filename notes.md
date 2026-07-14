atlas/
│
├── database/
│   ├── schema/
│   │   ├── 001_create_location.sql
│   │   ├── 002_create_location_type.sql
│   │   └── 003_add_indexes.sql
│   │
│   ├── migrations/
│   │   ├── 004_add_latitude.sql
│   │   └── 005_add_architect.sql
│   │
│   └── seed/
│       └── location_types.sql
│
├── backend/
│   ├── app/
│   ├── scripts/
│   │   ├── import_csv.py
│   │   ├── sync_wikipedia.py
│   │   └── rank_locations.py
│   │
│   └── requirements.txt
│
├── frontend/
│
└── README.md

Paradise-Atlas/
│
├── api/
│   ├── main.py
│   │
│   └── app/
│       ├── __init__.py
│       ├── database.py
│       │
│       ├── routers/
│       │   ├── __init__.py
│       │   ├── theatres_router.py
│       │   ├── locations_router.py
│       │   ├── visits_router.py
│       │   ├── digs_router.py
│       │   └── capitals_router.py
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   ├── theatre_services.py
│       │   ├── location_services.py
│       │   ├── visit_services.py
│       │   ├── digs_services.py
│       │   └── capital_services.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   ├── theatre.py
│       │   ├── location.py
│       │   └── visit.py
│       │
│       └── schemas/
│           ├── __init__.py
│           ├── theatre_schema.py
│           ├── location_schema.py
│           └── visit_schema.py
│
├── database/
│   ├── schema/
│   │   ├── reset_db.sh
│   │   ├── get_flat_files.py
│   │   ├── 001_create_tables.sql
│   │   ├── 002_seed_data.sql
│   │   ├── 003_import_paradise_voyage.sql
│   │   └── ...
│   │
│   └── flat_files/
│       ├── paradise_voyage_raw_data.csv
│       └── ...
│
├── maps/
│   ├── generate_theatre_map.py
│   ├── generate_visit_map.py
│   ├── generate_city_map.py
│   └── output/
│       ├── theatres.html
│       ├── visits.html
│       └── cities.html
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │       └── theatres.js
│   │
│   ├── templates/
│   │   ├── theatres.html
│   │   └── visits.html
│   │
│   └── index.html
│
├── tests/
│   ├── test_theatres.py
│   ├── test_locations.py
│   └── test_visits.py
│
├── requirements.txt
├── README.md
└── .gitignore

Paradise-Atlas/
│
├── api/
│   ├── main.py
│   └── app/
│       ├── routers/
│       ├── services/
│       └── database.py
│
├── database/
│   └── schema/
│
├── maps/
│   ├── generate_theatre_map.py
│   └── output/
│
└── frontend/
    ├── index.html
    ├── css/
    │   └── style.css
    └── js/
        └── map.js


            select 
            	l.name as city,
            	l.state_province as state_province,
            	l.country  as country,
            	l.latitude  as latitude,
            	l.longitude  as longitude, 
            	v.date as visit_date,
            	v.visit_order  as visit_order,
            	d.address  as digs_address,
            	d.longitude  as digs_logitude,
            	d.latitude as digs_latitude,
            	d.digs_type_id as digs_type_id,
            	t.name as theatre_name,
            	t.address as theatre_address,
            	t.latitude as theatre_latitude,
            	t.longitude as theatre_longitude
           	from location l
            join visit v on v.location_id = l.id
            join digs d on d.id = v.digs_id
            join theatre t on t.id = v.theatre_id 
            where l.id = 278;