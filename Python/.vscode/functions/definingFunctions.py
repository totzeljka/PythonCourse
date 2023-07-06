# parametar je input koji definisemo za nase funkcije first_name, last_name
# arguent je stvarna vrednost nekog parametra "Zeljka", "Tot"

def greeting():
    print("Hello")
    print("Welcome to python programing!")

greeting()



def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome to python programing!")
greet("Zeljka", "Tot")

#vratice isprintano sta treba i none jer svaka fja vraca
print(greet("Zeljka Tot"))




#tipovi funkcija: funkcije se mogu podeliti u dve velike kategorije: one koje racunaju i one koje izvrsavaju

def get_greeting(name):
    return f"Hi (name)!"

message = get_greeting("Zeljka")
file = open("content.txt", "w")
file.write (message)


#key word argumen, koristimo da kod bude jasniji i citljiviji
def increment(number, by):
    return number+by
print(increment(2,by=1))



#mozemo definisati i overridovati
def increment1(number, by=1):
    return number+by
print(increment(2))

def increment2(number, by=1):
    return number+by
print(increment(2, 5))