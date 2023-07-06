from pathlib import Path


# prvo iz pathlib modula importujemo klasu Path
# apsoluth path
Path("C\\Program Files\\MyFolder")
# relative path koristeci raw string
Path(r"C:\Program Files\MyFolder")
# na maku ili linuksu aplolutni put
Path("/usr/local/bin")
# path objekat koji predstavlja trenutno korisceni folder
Path()
# related path
Path("classes/__init.py")
# kombinovanje dva path-objekta
Path() / Path("classes")
# kombinovanje puta sa stringom ili vise stringova
Path() / "classes" / "__init__.py"
# vraca  home direktorijum trenutnog usera
Path.home


path = Path("classes/__init.py")


print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.with_name("file.txt"))
print(path.absolute)
print(path.with_suffix(".txt"))
print(path)
