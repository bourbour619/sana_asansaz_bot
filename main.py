# This Python file uses the following encoding: utf-8
import sys
import os

from gui.app import App
from core.database import DB

if __name__ == "__main__":
    # config database
    db_instance = DB()
    db_instance.migrate_tables()

    # create data folder
    if not os.path.exists('data'):
        os.mkdir('data')

    app = App(sys.argv)
    # ...
    sys.exit(app.exec())
