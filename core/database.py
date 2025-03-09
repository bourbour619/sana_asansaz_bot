from pathlib import Path
from urllib.parse import quote_plus

import win32com.client
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

if __package__ == 'core':
    from core import models
else:
    import models


base_dir = Path(__file__).resolve().parent.parent

Base = declarative_base()


class DB:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._connection = None
        return cls._instance
    
    def create_access_db(self):
        engine = win32com.client.Dispatch("DAO.DBEngine.120")
        engine.CreateDatabase(base_dir / 'Database.accdb', ";LANGID=0x0409;CP=1252;COUNTRY=0", 64)
        print(f"Database created at %s" %(base_dir / 'Database.accdb'))

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
                                 models.Config.__table__,
                                   models.Post.__table__,
                                     models.SanaItem.__table__,
                                     models.Attachment.__table__], checkfirst=True)
