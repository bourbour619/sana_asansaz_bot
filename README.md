
# ربات آسان ساز ثنا :|


## ساخت .exe

دستور زیر را در cmd وارد کنید

```bash
 pyinstaller --onefile --add-data "data;data" --add-data "staticfiles;staticfiles" ^
        --add-data "./venv/Lib/site-packages/PySide6/plugins;PySide6\plugins" ^
        --add-data "Database.accdb;." --add-data ".env;." ^
        --clean --icon="./staticfiles/adliran.ico" ^
        --name="ربات آسان ساز ثنا" main.py
    