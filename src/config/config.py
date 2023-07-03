import os
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
# from dotenv import load_dotenv

# from decouple import config
# load_dotenv()
class Config:
    DB_USER = os.getenv("PGUSER")
    DB_PASSWORD = os.getenv("PGPASSWORD")
    DB_NAME = os.getenv("PGDATABASE")
    DB_HOST = os.getenv("PGHOST")
    DB_CONFIG = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

conf = ConnectionConfig(
   MAIL_USERNAME="pithadiyakunal17@gmail.com",
   MAIL_PASSWORD="kunal@123",
   MAIL_PORT=587,
   MAIL_SERVER="smtp.gmail.com",
   MAIL_STARTTLS = True,
   MAIL_SSL_TLS = False,
   USE_CREDENTIALS = True,
   VALIDATE_CERTS = True,
   MAIL_FROM = "pithadiyakunal@gmail.com"
)


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL="postgresql://postgres:postgres@localhost:5432/verify.db"
# engine= create_engine(DATABASE_URL)
# SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Base=declarative_base()

