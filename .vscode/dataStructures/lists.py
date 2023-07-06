# liste se definisu []

letters1 = ["a", "s", "d", "f"]
matrix = [[0, 1], [2, 3]]

# ako zelimo listu od 1000 nula
zeros = [0]*1000
print(zeros)

# liste mogu da se kombinuju ne moraju biti istog tipa
combined = zeros + letters
print(combined)

# ako zelimo da nesto broji do nekog broja npr 19
numbers = list(range(20))
print(numbers)


# mozemo da iteriramo po stringu
chars = list("Zdravo svima koliko vas ima!")
print(chars)
print(len(chars))


letters = ['Z', 'd', 'r', 'a', 'v', 'o', ' ', 's', 'v', 'i', 'm', 'a', ' ',
           'k', 'o', 'l', 'i', 'k', 'o', ' ', 'v', 'a', 's', ' ', 'i', 'm', 'a', '!']
print(letters)

# da nam stampa slovo po indeksu
print(letters[2])
# drugo od pozadi
print(letters[-2])
# da zameni slovo tj element iz liste
letters[0] = "z"
print(letters)

# da sece string -originalna nista je nepromenjena
print(letters[0:6])
print(letters[0:])
print(letters[:3])

# svaki drugi elemet liste
print(letters[::2])


# svaki peti elemet liste
print(letters[::5])

# da ispise obrnutim redom

# svaki drugi elemet liste
print(letters[::-1])


# unpaking lists
numbers = [1, 2, 3, 4, 4, 4, 44, 4, 4, 4, 4, 4, 44, 7]

# numbers = [1,2,3,4]
# first = numbers[0]
# second =numbers[1]
# third = numbers[2]
# isto kao i
# first, second, third = numbers

first, second, *other = numbers
print(first)
print(second)

first, *other, last = numbers
print(first)
print(last)
print(other)


# looping over lists
# enumerate funkcija vraca tuple

letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)


# adding itemf to lists
# at the end of the list
letters.append("d")

# adding item in specific place in list
letters.insert(2, "lj")
print(letters)


# removing itemf from lists
# da obrise samo jedno slovo
letters.pop(1)
print(letters)
# da obrise slovo c-samo jednom se ponavlja ako ima vise slova moramo ponoviti
letters.remove("c")
print(letters)
# brise sve do oreddjenog rendza
del letters[0:2]
print(letters)
# ukljanja sve objekte sa liste
letters.clear()
print(letters)


# finding items in list
letters = ["a", "b", "c"]
print(letters.index("a"))
# ValueError: 'd' is not in list
print(letters.index("d"))
# ovako ne vraca gresku
if "d" in letters:
    print(letters.index("d"))


# sorting lists

numberz = [3, 51, 23, 14, 78, 46]
print(numberz)

# sortira unazad od najveceg ka najmanjem
numberz.sort(reverse=True)
# pravi novu listu dok je originalna neizmenjena
print(sorted(numberz))
print(numberz)


# zip function
# spajanje dve liste

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# stampace [(1, 10), (2, 20), (3, 30)]
print(list(zip(list1, list2)))

# stampace [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
print(list(zip("abc", list1, list2)))
