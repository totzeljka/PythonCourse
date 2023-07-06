import requests


# u cmd kucam pip3 install requests, da bih upgragovala pip kucam pip3 install --upgrade pip
# i za jos updatea To update, run: python.exe -m pip install --upgrade pip pisace u cmd sta treba svakako
# potom kad imam najnoviju verziju  idem na pip3 list:

# C:\Users\zeljka.tot>pip3 list
# Package            Version
# ------------------ --------
# certifi            2023.5.7
# charset-normalizer 3.1.0
# idna               3.4
# pip                23.1.2
# requests           2.31.0 --semantic versioning : vrezija glavna. manja verzija. i bugfixes
# setuptools         65.5.0
# urllib3            2.0.3


# moguce je raditi jos razne radnje sa ovim:
# da bih instalirala neku konkretnu verziju  u cmd kucam: pip3 install requests==2.9.0
# da bih instalirala najnoviju kompatibilnu verziju  u cmd kucam: pip3 install requests==2.9.*
# da uninstaliram: pip3 uninstall requests i y kao potvrdu kad zatrazi
# da bih instalirala najnoviju kompatibilnu verziju  u cmd ponovo kucam: pip3 install requests==2.9.*, vratice mi da je to2.9.2
# opet uninstaliram pa pip3 install requests==2.*, vratice mi najnoviju kompatibilnu verziju 2., meni je to 2.31.0
# mogu da odem pu pypi.org i proverim koja je najnovija , kao i da procitam dokumentaciju vezanu za paket

# responce 200 uspesni 400eror...
responce = requests.get(
    "https://knowledgemaps.enlightitsourcing.com/auth/login")
print(responce)


# kako se objavljuju svoji paketi:
# napraviti nalog na pipy i potvrditi aktivaciju mejla
# u cmd kucamo:
# pip3 instal setuptools wheel twine
# mkdir zeljkapdf
# cd zeljkapdf
# code .
# u code napravimo novi folder koji se zove isto kao folder gore u mom slucaju je zeljkapdf i pisemo kod tu,
# treba da ima __init__ faj obavezno, i jos tri fajla, setup.py, readme i licence
# u rootu projekta fravimo fajl setup.py i u njemu  pisemo

# import setuptools
# from pathlib import Path

# setuptools.setup(

#     name = "zeljkapdf",
#     version=1.0,
#     long_description=Path("README.md").read_text(),
#     packages= setuptools.find_packages(exclude = ["one koje zelimo da iskljucimo", "oni koji nemaju sorce kod"])
# )

# u rootu projekta pravimo fajl README.md i u njemu  pisemo  neki tekst npr     This is a homepage of our project!
# u rootu projekta pravimo fajl LICENCE fajl i u njemu  pisemo (na choosealicence.com postoje osnovni templejti za licence file, tu odaberem koji zelim i kopiram i pejstujem u moj licence fajl)


# u terminalu : python3 setup.py sdist bdist_weel, napravice mi se dva nova direktorijuma build i dais (u distu imam dva fajla: whl fajl i sorce distribution fajl, oba zipovana)
# u terminalu  twine upload dist/* , trazice username (kicam ono na koje sam registrovala nalog kao i password) i uploadovace i to mogu da proverim na sajtu

# za instalaciju u terminalu kucam : pipenv instal zeljkapdf, u mom projektu  kucam from zeljkapdf import modul koji sam napisala i onda mogu da koristim taj modul
