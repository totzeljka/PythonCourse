import random
import string

# uvek dobijemo neku drugu vrednost
print(random.random())

# nira jedan broj od niza
print(random.randint(1, 10))

# bira jedan od ponudjenih
print(random.choice([1, 2, 3, 4]))

# bira dva broja iz niza
print(random.choices([1, 2, 3, 4], k=2))

# bira bilo koja 4 slova iz navedonogstringa
print(random.choices("fidhgidhflihgdlifhihgifhihi", k=4))

# vraca jedan string umesto 4 zasebna slova iz nevedenog stringa
print("".join(random.choices("fidhgidhflihgdlifhihgifhihi", k=4)))

# daje sva slova mala i velika, samo mala ili samo velika
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

# daje  brojeve od 0-9
print(string.digits)

# umesto da dajemo neki stringh mpozemo pisati kao neki random password (56.8 billion possible combinations )
print("".join(random.choices(string.ascii_letters + string.digits, k=6)))


# ako definisemo  neke brojeve i primenimoishufle pomesace nam random
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
