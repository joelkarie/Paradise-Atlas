import os
from sqlalchemy import create_engine

# DATABASE_URL = os.getenv("DATABASE_URL") # Uncomment to ensure database is not running locally.
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+psycopg://joelkarie:@localhost/atlas_paradiso"
)
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)
