
items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 7)
]


filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

# sledeca dva reda su ista , list comprehensions
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]

# isto sto i u 9.
filtered = [item for item in items if item[1] >= 10]
