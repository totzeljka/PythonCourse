from pathlib import Path
from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:
#   for path in Path("classes").rglob("*.*"):
#       zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("classes")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
