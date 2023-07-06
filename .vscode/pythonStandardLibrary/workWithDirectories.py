from pathlib import Path


path = Path(".vscode")


# path.exists()
# path.is_file()
# path.is_dir()
# path.mkdir()
# path.rmdir()
# path.rename("newName")

for p in path.iterdir():
    print(p)

# daje listu Windows path objekata
paths = [p for p in path.iterdir()]
print(paths)

# daje listu  path objekata unutar zadatog stringa
paths1 = [p for p in path.iterdir() if p.is_dir()]
print(paths1)

#
py_files = [p for p in path.glob("**/*.py")]
# isto
py_files = [p for p in path.rglob("*/*.py")]
