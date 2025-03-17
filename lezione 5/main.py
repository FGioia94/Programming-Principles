# This is how we wrote our programs so far
print()
print()
print()
print()
print()
print()
print()
print()

# That said, there might be some cases though, where we might want to execute a certain part of code **only if a condition satisfied**
password = input("Inserisci la password: \n")
valid_password = "B4rtS1mps0n"

if password == valid_password:
    print("Accesso Consentito\n")
else:
    print("Password Errata\n")


temperature = 35
if temperature > 40:
    print("Accendi Sistema\n")

elif temperature > 70:
    print("INCENDIO! ATTIVA ESTINTORI!\n")

elif temperature < 10:
    print("Accendi Sistema Riscaldamento\n")

else:
    print("Temperatura Ideale\n")


name = input("Inserisci il tuo nome")
if name != "":
    print(f"Benvenuto {name}")

# I can write this using truthy/falsy:
if name:
    print(f"Benvenuto {name}")

user_logged_in = False

user_status = None
if user_logged_in:
    user_status = "active"
else:
    user_status = "inactive"

print(user_status)

# Also, i can use the ternary operator (shorter, more pythonic form, but don't overdo it otherwise it becomes hard to read)
# There is no elif for this syntax
user_status = "active" if user_logged_in else "inactive"


password = input("inserisci la password: \n")
if password == "B4rtS1mps0n":
    print("Accesso Consentito")

# To repeat this, we could use a while loop

password = None
while password != "B4rtS1mpson":
    password = input("Inserisci la password: ")
print("Accesso consentito")

# the keyword "break" forcefully breaks the loop
while True:
    password = input("Inserisci la password: ")
    if password == "B4rtS1mps0n":
        break

# the keyword "continue" restarts the loop
while True:
    password = input("Inserisci la password: ")
    if password == "B4rtS1mps0n":
        break
    if not password:
        continue
    print("Password Errata")
print("Accesso Consentito")


# In this case, the "else" executes only when the loop doesn't end because of a break or an error. So only if it finishes naturally
attempts = 0
while password != "B4rtS1mps0n":
    password = input(f"{attempts} - Inserisci la password: ")
    if attempts >= 2:
        break
    attempts += 1
else:
    print("Accesso Consentito")


# A for loop repeates some code based on a collection
# one of the main collections in python is the list

tasks = ["fare la spesa", "cucinare i fagioli", "lavare il cane"]
for task in tasks:
    print(task)

# we can use enumerate() to get also the number and the element:
for id, task in enumerate(tasks):
    print(id, task)

# the start arg specifies the start value for id, by default 0
for id, task in enumerate(tasks, start=1):
    print(id, task)

# we can also use the range function to range from one number to another
for i in range(2, 10):
    print(i)

# we can also use a step (even a negative one, a negative step would step backward)
for seconds in range(10, 0, -1):
    print(seconds)
    if seconds == 5:
        break 

# As in the while, the else gets executed only if the for loop terminates in a natural way, with no break or errors
for seconds in range(10, 0, -1):
    print(seconds)
    if seconds == 5:
        break  
else:
    print("you inputted less than 5 as a second term")

# ps. range can be converted to a list with the list() function