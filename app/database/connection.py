import os
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = sqlalchemy.create_engine(DATABASE_URL)

SessionLocal = sessionmaker(engine)
