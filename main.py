# This Python file uses the following encoding: utf-8
import sys
import os
import sqlalchemy.exc as alch_exc

from gui.app import App
from core.database import DB

if __name__ == "__main__":

    if getattr(sys, 'frozen', False):  # Running as .exe
        print(sys._MEIPASS)

    # # config database
    db_instance = DB()
    try:
        db_instance.migrate_tables()
    except alch_exc.DBAPIError:
        db_instance.create_access_db()
        db_instance.migrate_tables()

    # create data folder
    if not os.path.exists('data'):
        os.mkdir('data')

    app = App(sys.argv)
    # ...
    sys.exit(app.exec())
