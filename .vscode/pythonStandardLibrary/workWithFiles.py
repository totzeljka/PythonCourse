from pathlib import Path
from time import ctime
import shutil


path = Path("classes/classes.py")

# path.exists()
# path.rename("newName")
# path.unlink()
print(ctime(path.stat().st_ctime))

path.read_bytes()
path.read_text()


# za kopiranje fajla

source = Path("classes/classes.py")
target = Path()/"__init.py"
shutil.copy(source, target)
