from array import array

# u 99.9 %slucajeva koristimo liste, ali ako primetimo da imamp performance probleme mozemo umesto liste koristiti arrays, kad imamo veliku kolicinu podataka u listi

# tabela u kojoj prikazuju string koji opisuje objekte u listi :  https://docs.python.org/3/library/array.html


numbers = array("i", [1, 2, 3])


numbers.pop
numbers.remove
numbers[0]

# TypeError: 'float' object cannot be interpreted as an integer, ne moze da se menja u float!!!
# numbers[0] = 1.0
