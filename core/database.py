from pathlib import Path
from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

from .models import Config, Post, SanaItem, Attachment

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
        # engine = create_engine('sqlite:///%s/db.sqlite3' %base_dir, echo=True)
        conn_string = r"access+pyodbc:///?odbc_connect=" + \
            quote_plus(
                "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s/Database.accdb" % base_dir)
        engine = create_engine(conn_string, echo=True)
        return Session(engine, expire_on_commit=False)

    def migrate_tables(self):
        engine = create_engine('sqlite:///%s/db.sqlite3' % base_dir, echo=True)
        conn_string = r"access+pyodbc:///?odbc_connect=" + \
            quote_plus(
                "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s/Database.accdb" % base_dir)
        engine = create_engine(conn_string, echo=True)
        Base.metadata.create_all(engine, tables=[
                                 Config.__table__, Post.__table__, SanaItem.__table__, Attachment.__table__], checkfirst=True)
