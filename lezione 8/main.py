# OOP - Object Oriented Programming

car1 = {
    "brand": "Fiat",
    "max_speed": 200,
    "year": 2020,
    "is_electric":True,
}

car2 = {
    "brand": "Ferrari",
    "max_speed": 300,
    "year": 2010,
    "is_electric":False,
}



class Car:
    def __init__(self, brand, max_speed, year, is_electrical):
        self.brand = brand
        self.max_speed = max_speed
        self.year = year
        self.is_electrical = is_electrical

    def drive_fast(self):  
        print(f"La {self.brand} corre a {self.max_speed} km/h")

fiat = Car("Fiat", 200, 2020, True)
fiat = Car("Fiat", 200, 2010, True)

# init is automatically created once we create an object of the class

# __main__ is the current script