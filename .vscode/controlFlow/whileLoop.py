
#uzmi broj pa podeli sa dva , pa taj broj podeli sa dav pa tah nbroj podeli sa dva sve dok ne dedjes do nule
number = 200
while number >0:
    print(number)
    number//=2


command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)




#infinite loops

command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() != "quit":
        break



