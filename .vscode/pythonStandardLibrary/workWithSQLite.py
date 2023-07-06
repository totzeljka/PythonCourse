import sqlite3
import json
from pathlib import Path


movies = json.loads(Path("movies.json").read_text())
# stampa listu diksinerija
print(movies)


# zagooglati db browser for sqlite, odabrati sqlitebrowser.org, na ovom websajtu kliknuti na downlad zip, kada se otvori brovzer idem na open database u direktorijumu projekta naci db.sqlite3 fajl,
# otvoriti ga, cvuda ce biti (0), kliknuti na create table , dati naziv Movies i ici na add field  id integer i PK, dodam sledece Title text, dodam sledece Year integer
# pa ok
# ovo koristimo da unesemo podatke u tabelu
# with sqlite3.connect("db.sqlite3") as conn:
#    command = "INSERT INTO Movies VALUES(?,?,?)"
#    for movie in movies:
#        conn.execute(command, tuple(movie.values()))
#    conn.commit()

# da iscitamo podatke iz tabele
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    for movie in movies:
        cursor = conn.execute(command)
        for row in cursor:
            print(row)


# da iscitamo podatke iz tabele u vidu tupels
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    for movie in movies:
        cursor = conn.execute(command)
    movies = cursor.fetchall()
    print(movies)
