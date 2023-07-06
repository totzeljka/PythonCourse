

#stampa :(1, 2, 3, 4, 5)

[1,2,3,4,5]
def multiply (*numbers):
    print (numbers)

multiply(1,2,3,4,5)


#stampa:
# (1, 2, 3, 4, 5)
#(1, 2, 3, 4, 5)
#(1, 2, 3, 4, 5)
#(1, 2, 3, 4, 5)
#(1, 2, 3, 4, 5)

def multiply (*numbers):
    for number in numbers:
        print (numbers)

multiply(1,2,3,4,5)


#stampa 120
def multiply (*numbers):
    total=1
    for number in numbers:
       # total = total* number        isto kao i 
        total *= number
    return total

print (multiply(1,2,3,4,5))


