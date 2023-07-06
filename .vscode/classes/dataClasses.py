from collections import namedtuple

# kada se jednom kreiraju ne moze se promeniti

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(1, 2)
print(p1 == p2)
