
---

# 🧭 Atlas Startup Checklist (Daily / Session Restart)

## 1. Open project in VS Code

* Open your Atlas root folder
* Confirm you see:

  * `scripts/`
  * `data/`
  * `ATLAS_NOTES.md`
  * `.gitignore`

---

## 2. Activate Python environment

```bash id="s1"
cd path/to/atlas
source venv/bin/activate
```

Confirm:

```bash id="s2"
which python
```

Should point to `venv`.

---

## 3. Check PostgreSQL is running

```bash id="s3"
brew services list
```

You want:

```text id="s4"
postgresql ... started
```

If not:

```bash id="s5"
brew services start postgresql
```

---

## 4. Connect to Atlas database

```bash id="s6"
psql atlas
```

Then verify:

```sql id="s7"
\dt
```

You should see your tables:

* `locations`
* `location_types`
* `raw_locations` (if still present)

---

## 5. Quick database health check

Run:

```sql id="s8"
SELECT COUNT(*) FROM locations;
SELECT COUNT(*) FROM location_types;
```

This confirms:

* DB is alive
* data exists

---

## 6. Run your ETL script (only if needed)

If you made changes:

```bash id="s9"
python scripts/import_csv.py
```

Then re-check:

```sql id="s10"
SELECT * FROM locations LIMIT 5;
```

---

## 7. Confirm schema integrity (important step)

```sql id="s11"
\d locations
\d location_types
```

You are checking:

* columns exist
* foreign keys exist
* structure hasn’t drifted

---

## 8. Resume work from ATLAS_NOTES.md

Open:

```text id="s12"
ATLAS_NOTES.md
```

Update or read:

* what you did last session
* what is broken
* next planned step

---

# 🧠 Core mental model (VERY important)

Every session should follow:

```text id="s13"
1. Environment ready (venv)
2. Database alive (Postgres)
3. Schema verified (tables exist)
4. Data verified (counts)
5. Work continues (ETL or SQL)
```

---

# 🧩 Optional “power upgrade” (highly recommended later)

Add a `Makefile` so you can do:

```bash id="s14"
make start-db
make shell
make run
```

or a simple `atlas.sh` script.

---

# 📦 Minimal “Atlas startup script” (optional)

Create:

```bash id="s15"
scripts/start.sh
```

```bash id="s16"
#!/bin/bash

echo "Activating venv..."
source venv/bin/activate

echo "Checking Postgres..."
brew services list | grep postgresql

echo "Ready. Connect with: psql atlas"
```

Run:

```bash id="s17"
bash scripts/start.sh
```

---

# 🚀 What this gives you

With this checklist, Atlas becomes:

* reproducible
* structured
* recoverable
* professional-grade workflow
* no “lost context” sessions

---

# 🧭 If you want next upgrade

Next step after this is very powerful:

## 👉 “Atlas Initialization Script”

One command that:

* starts Postgres
* activates venv
* checks schema
* optionally runs migrations

That’s how real backend systems are operated.

Just tell me when you’re ready for that.

2. Simple relational model (recommended)
Visit
id (PK)
date/time
location_id (FK → Location)
Location
id (PK)
name (e.g., “Boston”, “Yosemite National Park”)
location_type_id (FK → LocationType)
LocationType
id (PK)
name (City, Landmark, National Park, Museum, etc.)
optional: description, hierarchy, rules