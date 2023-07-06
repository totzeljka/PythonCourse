# xxxxx.py se zovu moduli, kao klase u javi, da bih uvela neku funkciju (metodu) iz drugog modula (klase) pisem from i ime modula
# i onda import pa ctrl space i tu cemo pokazati sve metode tj funkcije i objekte koje imam definisane, odvajam ih zarezom,
# da uvedem sve * ovo nije dobra praksa
# drugi nacin je da se napise import pa ime modula import lists npr
# ovo vazi ako se nalaze u siom folderu tj paketu ili prpadaju  object klasama

from classes import another, other
import sys

# pacages:
# dodaje se subdirectory i __init__.py fajl u svaki kako bi python tretirao folder kao paket - kontejner za jedan ili vise modula
# kada se poziva kao u javi, ovjekt klase . metoda  (from classes-foldertj paket, import classes-modul)

from classes import classes

# subpaketi
# fajl unutar  fajla

# apsolute import:
from modules.subPackage import subModule
# relative import
from . subPackage import subModule


print(sys.path)
classes.another
subModule.greetings


# dir function koristi se za debugging, dobia se array stingova svih atributa i metoda definisanih u objektu
print(dir(classes))

print(classes.__name__)
print(classes.__path__)
