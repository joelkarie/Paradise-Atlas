from fastapi import FastAPI
from sqlalchemy import create_engine, text

# Start Uvicorn
# uvicorn app.main:app --reload
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Atlas Paradiso API"}


DATABASE_URL = "postgresql+psycopg://joelkarie:@localhost/atlas_paradiso"

engine = create_engine(DATABASE_URL)
