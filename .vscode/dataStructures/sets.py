# setovi su neuredjeni za razliku od lista
numbers = [1, 2, 1, 3, 2, 3, 4, 5]
second = {1, 4}


first = set(numbers)
print(first)


second.add(16)
second.remove(4)
print(second)

# unija dva seta
print(first | second)

# presek setova
print(first & second)

# razlika dva seta
print(first-second)
print(second - first)

# symetric diference- ono sto ima ili u prvom ili u drugom ali ne u oba
print(first ^ second)

# u setovima ne mozemo pristupitu objektu po indeksu!
#
