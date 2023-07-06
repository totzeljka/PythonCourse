from timeit import timeit


# displaying proper error messages, exceptions

# e.g. IndexError: list index out of range
numbers = [1, 2]
print(numbers[3])


# to handle  value error we need to put statement in try block
try:
    age = int(input("Age: "))
except ValueError:
    print("You did not enter valid age.")
else:
    print("No exceptions were trown.")
print("Execution continues.")


# multiple messages
try:
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You did not enter valid age.")
except ZeroDivisionError:
    print("Age cant be 0")
else:
    print("No exceptions were trown.")
print("Execution continues.")


# finaly clause-uvek se izvrsava, za sporlje resurse: da se zatvore fajl, database connections, network connetions...
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You did not enter valid age.")
else:
    print("No exceptions were trown.")
finally:
    file.close()


# kraci i jednostavniji bez finaly
try:
    with open("app.py") as file:
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You did not enter valid age.")
else:
    print("No exceptions were trown.")


# raising exceptions : https://docs.python.org/3/library/exceptions.html
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cnnot be 0 or less.")
    return 10/age

# ako dam -1 treba da mi istampa:ValueError: Age cnnot be 0 or less.
# calculate_xfactor(-1)


# ako okruzimo try catch blokom onda ce lepo da ispise
try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


# cost of rasing exceptions, brzi je drugi ali nije osetljivo, bolje if , ne koristiti exceptions osim ako bas mora

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cnnot be 0 or less.")
    return 10/age
try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""
print("first code= ", timeit(code1, number=10000))


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor=  calculate_xfactor(-1)
if xfactor ==None
pass
"""
print("first code= ", timeit(code1, number=10000))
print("second code= ", timeit(code2, number=10000))
