# class: human- pascal naming conv.
# object: Zeljka, Laza , Filip

# metode koje definisemo u klasi treba da imaju barem jedan parametar koji se po konvenciji zove self, ona referencira trenutni objekat sa kojim se radi
# kada se metoda pozove objektom na ovakav nacin, ne moramo da obezbedjujemo parametre, piton interpreter to radi za nas

# atributi na nivou klase koriste sve instance klase
class Point:

    default_color = "red"

    # magicne metode pajtona , imaju dva underskora na pocetku i na kraju u svom nazivu i automatski se pozivaju
    # pajton interpreterom npr init metoda se automatski poziva kada se kreira objekat point = Point(1, 2)
    # https://rszalski.github.io/magicmethods/
    # imamo razne za definisanje objekta za poredjenje, za matematicke operacije...

    def __init__(self, x, y):
        self.x = x
        self.y = y

     # pretvara pointu string
    def __str__(self):
        print(f"Point({self.x},{self.y})")

    # koriste za poredjenje objekata da li su equal ili greater jer ako bi samopozvali na jednakost objekata  pajton bi poredio mesto u memoriji za objekte i
    # bez obzira da li imaju istu vrednost nemaju istu vrednost u memoriji, za ovo su nam potrebnae magicne mtetode
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.x > other.y

    def __sdd__(self, other):
        return Point(self.x + other.x and self.x + other.y)

    # obicne metode

    def draw(self):
        print(f"Point({self.x}{self.y})")

    # class  decorator koristi se da promeni instance methode u class methode
    @classmethod
    def zero(cls):
        return cls(0, 0)


# objekti (instance klase) koriste metode draw npr
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)

point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()

point = Point.zero

point = Point(10, 20)
other = Point(1, 2)
print(point == other)
print(point > other)
print(point < other)


combined = point + other
print(combined.x)
