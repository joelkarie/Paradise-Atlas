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