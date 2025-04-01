class Car:
    # We can define class attributes here in the class body
    wheels = 4
    total_built_car = 0
    ##This makes the attibute PRIVATE
    __total_driven_km = 0 # Not accessible from outside of the class
    ##This makes the attibute PROTECTED
    _protected_attribute = 1 # Accessible from outside of the class
    
    def __init__(self, 
                 brand, 
                 max_speed, 
                 year, 
                 is_electric):
        
        self.brand = brand
        self.max_speed = max_speed
        self.year = year
        self.is_electric = is_electric

        # This will allow us to know how many total built car we have
        Car.total_built_car += 1

    def drive(self, kilometers):
        print(f"La {self.brand} guida per {kilometers} chilometri")
        Car.__total_driven_km += kilometers
    
    def get_total_driven_km(self):
        """
        Getter method for getting attribute
        """
        return(Car.__total_driven_km) 

car1 = Car("Fiat", 200.0, 2020, True)
car2 = Car("Ferrari", 300.0, 2010, True)
car1.drive(20)
car2.drive(100)

# INTROSPECTION
print(type(car1))
print(dir(car1)) # returns all methods and class attributes
print(car1.__class__) # this prints the class
print(dir()) # this prints the current scope
print(hasattr(car1, "brand")) # this prints the current scope
print(car1.__dict__) # returns a dictionary of the attributes
print(car1.__module__) # file where the class is defined
print(car1.__str__()) # returns the class as a string

# REFLECTION
# modifies the attributes **dynamically** during runtime

new_attr = input("Come vuoi chiamare il nuovo attributo da aggiungere? ")

setattr(car1, new_attr, 1500) # Setting a new attribute dynamically
print(car1.weight)

print(getattr(car1, new_attr)) # getting a new attribute dynamically



# NAME MANGLING - Syntax that allows us to access a private attribute from outside
car1._Car__total_driven_km += 2
print(car1._Car__total_driven_km)