from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set your database URL here (use your MySQL credentials)
DATABASE_URL = "mysql+pymysql://root:R123P@localhost/MySQL80"

# Set up the SQLAlchemy engine
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

# Create a session maker to interact with the DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models (tables)
Base = declarative_base()



