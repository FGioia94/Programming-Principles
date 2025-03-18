# Lists
 
client_0 = "Luisa"
client_1 = "Mario"
client_2 = "Anna"

# this is not very convenient

print(client_0)
print(client_1)
print(client_2)

# better
clients = ["Luisa", "Mario", "Anna"] # usually, it is suggested to call lists using plural

for client in clients:
    print(client)

# Lists properties:
    # Lists have an order
    # Mutability

clients[1] # "Mario"

# using an index out or range we get an indexError

clients[-1] # Last element
clients[-2] # element before the last one
# clients[-5] generates an index error too

clients[1:4] # slicing, this slices more than one element
clients[1:4:2] # this has steps too

# all other data types are not mutable, but the list is mutable
name = "Pippo"
print("Pippo")
name = "Pluto"
# Here i am not modifying the string, I am assigning the variable to a different type

# Here is how i can change the list:
clients[1] = "Marco"

clients.append("Nino")
clients.insert(2, "gianni") # adds at a specific position
clients.extend("Sandra", "Gino") # similar to +, but it is inplace
clients + ["Sandra", "Gino"] # is not inplace, generates a new list, so you need to do:
clients = clients + ["Sandra", "Gino"]

clients.remove("Mario")
clients.pop(2) # similar to remove, but it takes an index. if we don't pass an index, by default is -1. Return the object popped

del clients[2] # This removes also the element from memory
clients.clear() # This clears the list but it keeps that in memory

clients.sort() # orders the list element in alphabetical order
sorted(clients) # similar but .sort() is implace, sorted() is not
len(clients) # returns the lenght of the list

print("Pino" in clients) # prints True if "Pino" is in clients

female_clients = clients
female_clients.remove("Mario")
# This will change clients too!!! We are assigning a reference not duplicating the list, i am assigning the same address in memory
# we could use this syntax to generate a new list though

## All these are quite equivalent
female_clients = clients[:] # fastest, C based
female_clients = clients.copy() # still quite fast
female_clients = [client for client in clients] # slowest in performances


# we can loop a string too

name = "Homer Simpson"
for char in name:
    print(char)

# we can use slicing/indexing too
name[2]

list(name) # ['H', 'o', 'm', 'e', 'r', ' ', 'S', 'i', 'm', 'p', 's', 'o', 'n']

################

ingredients = ["butter", "jelly", "bread"]
sandwich = " & ".join(ingredients) # concatenates all elements in the list to a string, the string passed is the separator

sandwich.split(" & ") # returns back to the list

#################

# tupla
# Come una lista, ma non può essere modificata
days = ("Lun", "Mar", "Merc")
print(days[1])

# days.pop() this is a write operation, not a read operation, this will generate a runtimeError
# days[0] = "Sunday" same error here

# Tuple also has the property of unpacking
# a = 5
# b = 10
# c = 7

(a, b, c) = (5, 10, 7)
a, b, c = 5, 10, 7 #This is equivalent