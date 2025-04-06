from .database import engine, Base
from .models import Item

# Create all tables in the database (based on the models defined)
Base.metadata.create_all(bind=engine)
