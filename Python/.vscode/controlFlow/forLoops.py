# razliciti for loops
for number in range (3):
    print("Sending some message")


for number in range (3):
    print("Sending some message", number)



for number in range (3):
    print("Sending some message", number+1)



for number in range (3):
    print("Sending some message", number+1, (number+1)*".")




for number in range (1,4):
    print("Sending some message", number, *".")



for number in range (1,10,2):
    print("Sending some message", number, *".")


#for else

syccessful = True
for number in range (3):
    print("Atempt")
    if syccessful:
        print("Successful!")
        break
else:
    print("Attempted 3 times and failed. :( ")