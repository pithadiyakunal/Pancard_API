from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
# from dotenv import load_dotenv


DATABASE_URL="postgresql://postgres:postgres@localhost:5432/verify_db"
# load_dotenv()
# DB_USER = os.getenv("PGUSER")
# DB_PASSWORD = os.getenv("PGPASSWORD")
# DB_NAME = os.getenv("PGDATABASE")
# DB_HOST = os.getenv("PGHOST")
# DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()


