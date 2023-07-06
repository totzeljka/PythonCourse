class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor")
        self.weight = 2
        super().__init__()

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

print(m.age)
print(m.weight)
