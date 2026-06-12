from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://joelkarie:@localhost/atlas_paradiso"

engine = create_engine(DATABASE_URL)
