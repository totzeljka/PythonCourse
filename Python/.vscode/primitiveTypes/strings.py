#Strings
course_name = "Python Course"

#duzina stringa
print(len(course_name))

#prvo slovo
print(course_name[0])

#stampa zadnje slovo
print(course_name[-1])

#uzima samo prva tri karaktera
print(course_name[0:3])

#stampa ceo string od pocetka
print(course_name[0:])

#stampa od cetvrtog slova do kraja
print(course_name[3:])

#ako unutar stringa koristimo " ili \ onda koristimo \' ili \\ moze i za jednostruke i za dvostruke 
course = "Course \"CodeWithMosh"
course1 = "Course\\CodeWithMosh"
course2 = "Course\'CodeWithMosh"
course3 = "Course\nCodeWithMosh"

print(course)
print(course1)
print(course2)
print(course3)

#ako imamo dva stringa , konkatencije stringova
first = "Zeljka"
second = "Tot"
#jedan nacin:
full = first+" "+ second
print(full)

#drugi nacin:
full_name=f"{first} {second}"
print(full_name)

#strings methods  course.   pojavice mi se sve metode za taj string
print(course_name)
print(course_name.upper())
print(course_name.lower())



#strip skida sve razmake , rstrip kraj, lstrip pocetak
course4 = "      Python course     "
print(course4.strip())
print(course4.rstrip())
print(course4.lstrip())


#trazi na kom se mestu nalazi neka sekvenca karatktera,Paziti na velika slova posto se obavezno gleda da li je malo ili veliko: ako nema  rez je -1
print(course4.find("cou"))
print(course4.find("pyt"))

#moze da se zameni slovo
print(course4.replace("c", "W"))


#proverava da li u stringu ima li slova, booleon , vraca true /false
print("pro" in course4)
print("swift" not in course4)








