#

# stampa start i 1
def multiply(*numbers):
    total = 1
    for number in numbers:
       # total = total* number        isto kao i
        total *= number
        return total


print("Start")
print(multiply(1, 2, 3))


# treba da dobijemo 6
def multiply(*numbers):
    total = 1
    for number in numbers:
       # total = total* number        isto kao i
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))

# debugging je tehnika kojom mozemo naci i popraviti bug
# klikne se na ikonicu levo trougao sa bubom
# ovo ce da generise novi fajl
# stisnem gde zelim da stavim break point i stisnem F9 pa F5 da pokrenem funciju do breaka i videcu da ce ta linija ce da se zeleni
# potom stisnem F10 jednam stajtment po stejtment
# kada dodjem do sumnjivog dela na toj liniji stisnem f11 da udjem u fju videcu da ulazi u funkciju i ici ce red po red u funkciji sa f10
# sa shift f5 se izlazi iz debaga
