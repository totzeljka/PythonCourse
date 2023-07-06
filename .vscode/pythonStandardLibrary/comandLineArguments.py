import sys


# u treminalu napisem dodatno argumente

print(sys.argv)
# ako user ne da nikake argumente treba da ispise Usage: python3 comandLineArguments.py<password>,
# ako da neki argument     Password i to sto je korisnik uneo

if len(sys.argv) == 1:
    print("Usage: python3 comandLineArguments.py<password>")
else:
    password = sys.argv[1]
    print("Password", password)

# u terminalu kucam $ptyhon3 comandLineArguments.py(ili kako mi se vec zove fajl u kom radim), izaci ce mi prva poruka,
# njemu je ovo bilo u prvoj liniji , ako se nalazi u nekom od paketa ili subpaketa onda kucam putanju do njega
# ako to ponovim i dokucam jos 1234 izace mi druga poruka da je Password 1234
