import sqlite3 as sql
db = sql.connect("Documents/SQL/chinook.db")
sorgu = """
SELECT * FROM V_ALBUM_OZET"""
cur = db.cursor()
cur.execute(sorgu)
print(cur) # <sqlite3.Cursor object at 0x7fd70fbf0c70>
print(cur.fetchone()) # (1, 'AC/DC', 1, 'For Those About To Rock We Salute You', 'For Those About To Rock (We Salute You)')
print(cur.fetchmany()) # [(1, 'AC/DC', 1, 'For Those About To Rock We Salute You', 'Put The Finger On You')]
print(cur.fetchall()) # [(1, 'AC/DC', 1, 'For Those About To Rock We Salute You', "Let's Get It Up"), (1, 'AC/DC', 1, 'For Those About To Rock We Salute You', 'Inject The Venom'), (1, 'AC/DC', 1, 'For Those About To Rock We Salute You', 'Snowballed')]
db.close()