#lokalne promenljive, ne postoje van metoda ako bi napisali metodu greet i onda van metode pokusali da stampamo poruku dobili bi gresku

def greet():
    message = "a"

#print (message)

#globalne promenljive, stampa a

message = "a"
def greet():
    message="b"
print(message)


#stampace b
def greet():
    global message
    message = "b"
print(message)

