from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

from .model import Config, Post, SanaItem, Attachment

base_dir = Path(__file__).resolve().parent.parent

Base = declarative_base()

class DB:

    _instance = None

    def __new__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__new__(cls, *args, **kwargs)
                cls._instance._connection = None
            return cls._instance

    def get_session(self):
        engine = create_engine('sqlite:///%s/db.sqlite3' %base_dir, echo=True)
        return Session(engine, expire_on_commit=False)


    def migrate_tables(self):
        engine = create_engine('sqlite:///%s/db.sqlite3' %base_dir, echo=True)
        Base.metadata.create_all(engine, tables=[Config.__table__, Post.__table__, SanaItem.__table__,Attachment.__table__], checkfirst=True)
