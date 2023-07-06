# AND OR NOT

high_income = False
good_credit = True
student = True

#Not elegible
if high_income and good_credit:
    print("Eligible")
else: print("Not elegible")

#Eligible
if high_income or good_credit:
    print("Eligible")
else: print("Not elegible")

#Elegible
if high_income or (good_credit and student):
    print("Eligible")
else: print("Not elegible")

#Not elegible
if  (high_income or good_credit) and not student:
    print("Eligible")
else: print("Not elegible")



#short-curcuit evaluation- cim nadje nesto sto ofgovara prestaje, cim dodje do good_credit prestaje
if  high_income or good_credit or student:
    print("Eligible")

    