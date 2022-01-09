import sqlite3 as sql

try:
    db = sql.connect("Documents/SQL/chinook.db")
    cur = db.cursor()
    artistAdi = input("ArtistAdı Giriniz")
    cur.execute(f"""INSERT INTO artists (Name)
    VALUES ({artistAdi})""")
except Exception as hata:
    db.rollback()
    print(hata)
else:
    db.commit()
finally:
    db.close()