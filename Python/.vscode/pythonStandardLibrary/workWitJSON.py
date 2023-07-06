import json
from pathlib import Path

# da napravimo jsom fajl
# movies = [
#   {"id": 1, "title": "Terminator", "year": 1989},
#   {"id": 2, "title": "Bulit Train", "year": 2000},
#   {"id": 3, "title": "50 first dates", "year": 1998}
#   ]

# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)


# da ucitamo json fajl
data = Path("movies.json").read_text()
movies = json.loads(data)
# da ucita sve
print(movies)
# da ucita samo prvi unos
print(movies[0])
# da ucita samo naslov drugog
print(movies[1]["title"])
