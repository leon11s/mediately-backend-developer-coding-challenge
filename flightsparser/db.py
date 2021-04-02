from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Float, Integer

from flightsparser import NOTE_TABLE_NAME, DATABASE_CONN_URI

Base = declarative_base()


class Notes(Base):
    __tablename__ = NOTE_TABLE_NAME

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    destination = Column(String)
    temperature = Column(Float)
    note = Column(String)

    def __repr__(self):
        return f"<Notes(destination={self.destination}, temperature={self.temperature}, note={self.note})>"


class NotesTable:
    def __init__(self) -> None:
        self.db_uri = DATABASE_CONN_URI
        self.table_name = NOTE_TABLE_NAME
        self.engine = create_engine(DATABASE_CONN_URI)

    def insert():
        pass

    # @classmethod
    # def find_by_name(cls, session, name):
    #     return session.query(cls).filter_by(name=name).all()


#
# https://github.com/auth0-blog/sqlalchemy-orm-tutorial

# https://docs.sqlalchemy.org/en/14/orm/tutorial.html