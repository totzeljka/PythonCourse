# recnik se moze definisati na dva nacina:
point = dict(x=1, y=2)
# ili isto znaci samo drugacije napisano
point = {"x": 1, "y": 2}
print(point)


# nakon sto definisemo  vrednost promenljive mozemo menjati i deklarisati novu
point["x"] = 10
point["z"] = 20

print(point)


# mozemo proveriti imamo li neki vrednost, ako nema a u pointu neka vrati 0
print(point.get("a", 0))

# brisanje
del point["x"]


# kako se pise petlja u dictionary

for key in point:
    print(key, point[key])


# comprehensions : stampa [0, 2, 4, 6, 8] dobijamo listu
values = []
for x in range(5):
    values.append(x*2)
print(values)

# ili isto:    values =[x*2 for x in range(5)]


# ako zelimo da imamo kye-value parove, stampa {0: 0, 1: 2, 2: 4, 3: 6, 4: 8} dobijamo tuple

values = {}
for x in range(5):
    values[x] = x*2
print(values)

# iliti isto
values = {x: x*2 for x in range(5)}
print(values)


# ako napisemo dobijamo generator object
values = (x*2 for x in range(5))
for x in values:
    print(x)
