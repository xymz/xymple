import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection = os.path.join(os.path.dirname(__file__)) + "/xymple.db"
engine = create_engine("sqlite:///" + connection, convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False,
                                      bind=engine))
Base = declarative_base()
Base.query = session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)
