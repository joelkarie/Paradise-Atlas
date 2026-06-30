# Atlas Paradiso 🌎🗺️

An interactive personal travel atlas built with **FastAPI**, **JavaScript**, **Leaflet**, and **PostgreSQL**.

Atlas Paradiso transforms travel experiences into an interactive map. It allows locations to be explored visually, with custom markers, travel routes, ratings, highlights, and geographic information.

---

## Features

- 🗺️ Interactive map powered by Leaflet
- 📍 Custom location markers
- 🔢 Numbered markers showing travel order
- 🛣️ Routes connecting visited locations
- ⭐ Personal location ratings
- ✨ Location highlights and notes
- 🖼️ Location images and custom popups
- 🌎 Geographic statistics:
  - Total locations
  - Countries visited
  - States/provinces visited
  - Capitols visited
- 🔐 Admin interfaces for managing location information

---

## Screenshots

_Add screenshots here_

Example:

```
![Atlas Paradiso Map](screenshots/map.png)
```

---

## Tech Stack

### Backend
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy

### Frontend
- JavaScript
- HTML/CSS
- Leaflet.js

### Mapping
- Leaflet
- Thunderforest Outdoors tiles
- OpenStreetMap data

---

## Project Structure

```
Atlas-Paradiso/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   └── database/
│
├── frontend/
│   ├── index.html
│   ├── joel_admin.html
│   ├── michael_admin.html
│   ├── css/
│   └── assets/
│
├── static/
│   ├── images/
│   └── assets/
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/atlas-paradiso.git
cd atlas-paradiso
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=your_database_connection_string
THUNDERFOREST_API_KEY=your_api_key
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

Open:

```
http://localhost:8000
```

---

## Database

Atlas Paradiso stores location information including:

- Location name
- Coordinates
- Country
- State/province
- Visit order
- Ratings
- Highlights
- Images
- Geographic classifications

Example:

```json
{
  "location": "Tokyo",
  "country": "Japan",
  "visit_number": 12,
  "joel_star_rating": 5,
  "joel_highlights": "Amazing food and neighborhoods"
}
```

---

## Future Improvements

- [ ] Mobile optimization
- [ ] Location search
- [ ] Filtering by country/state/category
- [ ] Interactive travel timelines
- [ ] Expanded photo galleries
- [ ] Additional map styles
- [ ] User authentication

---

## About Atlas Paradiso

Atlas Paradiso began as a way to combine my interests in travel, geography, photography, and software development into one project.

The goal is to create a personal digital atlas where memories, journeys, and places can be explored through an interactive map.

---

## Author

**Joel Karie**

Software Developer | GIS Enthusiast | Traveler
