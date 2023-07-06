
items = [
    ("Product1", 10),
    ("Product2", 20),
    ("Product3", 7)
]

# sortirati po ceni


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

# drugi nacin da se ovo napise:
# items.sort(key = lambda parameters:expression)
items.sort(key=lambda item: item[1])
print(items)


# izvuci samo cene iz liste
prices = []
for item in items:
    prices.append(item[1])
print(prices)

# drugaciji nacin da se ovo odradi
map(lambda item: items[1], items)
print(prices)

# drugaciji nacin da se ovo odradi da istampa svaku ponaosob
x = map(lambda item: item[1], items)
for item in x:
    print(item)


# drugaciji nacin da se ovo odradi da istampa listu
prices = list(map(lambda item: item[1], items))
print(prices)
