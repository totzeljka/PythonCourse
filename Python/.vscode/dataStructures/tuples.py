# tuples su read only liste
# ne mogu se modifikovati

point = 1, 2

# prazan  tuple
ppoint = ()

# <class 'tuple'>
print(type(point))

# konkatenacija tuple-a (2, 3, 4, 5)
point1 = (2, 3) + (4, 5)
print(point1)

# ponavljanje itema tuple-a (2, 3, 2, 3, 2, 3, 2, 3)
point2 = (2, 3)*4
print(point2)


# list to tupple
lpoins = [1, 2, 3, 4]
poins = tuple([1, 2, 3, 4, 5, 6])

print(type(lpoins))
print(type(poins))

# stampa tuple od indeksa 0 do indeksa 2 -range
print(poins[0:2])

# TypeError: 'tuple' object does not support item assignment, tuple se ne moze menjati
# poins[0] = 10
