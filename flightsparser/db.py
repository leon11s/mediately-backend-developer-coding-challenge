from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text

from flightsparser import DATABASE_CONN_URI, NOTE_TABLE_NAME
from flightsparser.scrapers import DepartureData

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
        Base.metadata.create_all(self.engine)

    def insert(self, data: DepartureData):
        data = {
            "timestamp": data.timestamp,
            "destination": data.city,
            "temperature": data.temperature,
            "note": data.note,
        }
        statement = text(
            f"""INSERT INTO {self.table_name} (timestamp, destination, temperature, note) 
                VALUES (:timestamp, :destination, :temperature, :note);"""
        )
        with self.engine.begin() as con:
            con.execute(statement, data)
