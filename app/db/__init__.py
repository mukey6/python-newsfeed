from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()
def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()

  return g.db
def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()
# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
#The engine variable manages the overall connection to the database.
Session = sessionmaker(bind=engine)
#The Session variable generates temporary connections for performing CRUD
Base = declarative_base()
#The Base class variable helps us map the models to real MySQL tables.
def init_db():
  Base.metadata.create_all(engine)