# koristi se kad nam treba da se ne stampa lista vec pojedinacni brojevi

numbers = [1, 2, 3, 4]

# kao rezultat dobijem listu
print(numbers)

# dobijam pojedinacne brojeve
print(*numbers)

# da dobijem listu od 5 elemenata tj od 0-4 [0, 1, 2, 3, 4]
values = list(range(5))
print(values)

# umesto da koristim list funkciju koristim unpaking operator da dobijem isto [0, 1, 2, 3, 4]
values = [*range(5)]
print(values)

# mogu da kombinujem liste, stampace mi [1, 2, 'aaa', 4, 5, 'H', 'e', 'l', 'l', 'o']
first = [1, 2]
second = [4, 5]
values = [*first, "aaa", *second, *"Hello"]
print(values)


# mogu da kombinuje dictionary: {'x': 10, 'aaa': 100, 'y': 20, 'z': 1}
first = {"x": 1}
second = {"x": 10, "y": 20}
values = {**first, "aaa": 100, **second, "z": 1}
print(values)
