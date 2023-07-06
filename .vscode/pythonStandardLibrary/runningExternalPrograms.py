import subprocess


#  $dir for windows, (["ls", "-l"]) za linux

# daje detaljan pregled fajlova i direktorija u trenutnom direktorijumu
completed = subprocess.run(["dir"], shell=True, capture_output=True, text=True)

# daje koji je tip-instanca klase subproces: <class 'subprocess.CompletedProcess'>

print(type(completed))

# vraca koji smo argument koristili
print("args", completed.args)

# vraca ako je uspesno  0 bilo koja osim nule je greska
print("return", completed.returncode)

# ukoliko bi bilo greske (gore umesto 0 neki broj) pisalo bi koja je greska, ako je 0 pisace None
print("stderr", completed.stderr)

# obzirom da ne hvatamo output Non pise, output mi pise u terminalu,nekad zelimo da uhvatimo output nekog drugog programa ili \
# drugog prozora i da radimonesto sa tim podatkom, npr da ga sacuvamo u fajlu ili  ako hvatamo
print("stdout", completed.stdout)


# bez capture output rezultat je
# Volume in drive C is Windows
#  Volume Serial Number is D6D5-D43F

#  Directory of c:\Users\zeljka.tot\PythonCourse

# 05/07/2023  20:14    <DIR>          .
# 05/07/2023  20:14    <DIR>          ..
# 06/07/2023  07:26    <DIR>          .vscode
# 05/07/2023  16:20                86 data.csv
# 05/07/2023  17:21             8,192 db.sqlite3
# 05/07/2023  16:04                22 files.zip
# 05/07/2023  16:29               149 movies.json
# 24/05/2023  07:50           110,313 zeljka.jpg
# 05/07/2023  13:05    <DIR>          __pycache__
#                5 File(s)        118,762 bytes
#                4 Dir(s)  113,498,955,776 bytes free
# <class 'subprocess.CompletedProcess'>
# args ['dir']
# return 0
# stderr None
# stdout None


# sa capture output
# <class 'subprocess.CompletedProcess'>
# args ['dir']
# return 0
# stderr b''
# stdout b' Volume in drive C is Windows\r\n Volume Serial Number is D6D5-D43F\r\n\r\n Directory of c:\\Users\\zeljka.tot\\PythonCourse\r\n\r\n05/07/2023  20:14    <DIR>          .\r\n05/07/2023  20:14    <DIR>          ..\r\n06/07/2023  07:26    <DIR>          .vscode\r\n05/07/2023  16:20                86 data.csv\r\n05/07/2023  17:21             8,192 db.sqlite3\r\n05/07/2023  16:04                22 files.zip\r\n05/07/2023  16:29               149 movies.json\r\n24/05/2023  07:50           110,313 zeljka.jpg\r\n05/07/2023  13:05    <DIR>          __pycache__\r\n               5 File(s)        118,762 bytes\r\n               4 Dir(s)  113,493,241,856 bytes free\r\n'


complicatedScript = subprocess.run(
    "python3", "other.py", capture_output=True, text=True)

# daje koji je tip-instanca klase subproces: <class 'subprocess.CompletedProcess'>

print(type(complicatedScript))

# vraca koji smo argument koristili
print("args", complicatedScript.args)

# vraca ako je uspesno  0 bilo koja osim nule je greska
print("return", complicatedScript.returncode)

# ukoliko bi bilo greske (gore umesto 0 neki broj) pisalo bi koja je greska, ako je 0 pisace None
print("stderr", complicatedScript.stderr)

# obzirom da ne hvatamo output Non pise, output mi pise u terminalu,nekad zelimo da uhvatimo output nekog drugog programa ili \
# drugog prozora i da radimonesto sa tim podatkom, npr da ga sacuvamo u fajlu ili  ako hvatamo
print("stdout", complicatedScript.stdout)
