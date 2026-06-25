import os
from sqlalchemy import create_engine

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://joelkarie:@localhost/atlas_paradiso"
)
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)
