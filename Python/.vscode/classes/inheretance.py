class Animal:
    def eat(self):
        print("eat")


# Animal -parent, base class
# Mamal and Fish are child classes, sub classes, they inherit animal class and have all properties of animal class as well theirown
# pored definisanih sve klase nasledjuju magicne klase tj object class

class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
f = Fish()

print(m.eat)
print(m.walk)
print(f.eat)
print(f.swim)
print(f.__class__)


# multilevel inheretance:

class Bird(Animal):
    def hatch(self):
        print("hatch")


class Pinguin(Bird):
    pass


pinguin = Pinguin()
pinguin.eat
pinguin.hatch
