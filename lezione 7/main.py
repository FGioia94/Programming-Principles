clients = ["Luisa", 
           "Mario",
           "Piera",
           ] #It is a good practice adding the comma at the end too


# dictionary, perfect for showing key-value pairs

clients = {"Luisa": "331123456789",
           "Mario": "12345678900",
           "Piera": "331123456789"}

# dictionaries are ORDERED, but I can't have two equal keys
# dictionaries are mutable, like a list
# we can't assign a list to a dict key


car = {
    "color": "red",
    "price": 34_000,
    "year": 2024,
    "is_hybrid": True,
}

car["year"] # If the key is not present, we get a keyerror
car.get("model") # same, but we get None instead of an error if the key is not present
car.get("model", "NoModel") # We can also specify a default value if the key is not present as a second attribute
car.keys() # Returns all the keys
car.items() # Returns key and value pairs

for key in car.keys():
    print(key)

for key, val in car.items():
    print(key, val)

car.pop("color") # removes an element and returns the popped item
car.popitem() # this removes the last inserted item and returns the popped item
len(car)


panda = {
    "color": "red",
    "price": 35_000,
    "year": 2024,
    "is_hybrid": True,
}


punto = {
    "color": "green",
    "price": 25_000,
    "year": 2014,
    "is_hybrid": True,
}

discounted_price = panda["price"] * 0.7
if discounted_price > 20_000:
    discounted_price -= 100
print(discounted_price)

discounted_price = punto["price"] * 0.7
if discounted_price > 20_000:
    discounted_price -= 100
print(discounted_price)

# This contrasts with the DRY principle. DRY -> Don't repeat yourself

def get_discounted_price():
    discounted_price = punto["price"] * 0.7
    if discounted_price > 20_000:
        discounted_price -= 100
    print(discounted_price)

get_discounted_price() # this is better, but we are still hard coding the car type

# let's use a parameter instead

def get_discounted_price(price, bonus_discount = 100):
    discounted_price = price * 0.7
    if discounted_price > 20_000:
        discounted_price -= bonus_discount
    print(discounted_price)
    return discounted_price
get_discounted_price(panda["price"])

# parameter: we assign that to the function
# argument: the one that we assign to the parameter when we call the function

# i can also assign an arbitrary number of parameters

def get_discounted_price(price, *args):
    print(args)
get_discounted_price(panda["price"], 3, 4, "test_arg")

def get_discounted_price(price, **kwargs):
    print(kwargs)
get_discounted_price(panda["price"], test_kwarg = "test")

# scope is the area where the variable is visible
# a variable defined in a function is only visible inside that function
# a variable defined outside is visible everywhere


# 4! = 4x3x2x1
# 4! = 4x3x2x1

def factorial(n):
    print("-", n)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) # recursive function

print(factorial(4))