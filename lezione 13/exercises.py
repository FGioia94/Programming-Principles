"""Modifica il seguente codice, applicando le linee guida
per una corretta formattazione e documentazione.
Opzionalmente, fatti aiutare da linter e autoformatter,
come flake8, autopep8 e ruff.
"""

class Person:
    """A class representing a person.

    Attributes:
        name (str): The name of the person.
        age (str): The age of the person.
    """

    def __init__(self, name, age):
        """Used to initialize basic attributes"""

        self.name = name
        self.age = age
        self._address = ''

    def set_address(self, address):
        """Used to set address"""

        self._address = address

    def get_address(self):
        """Used to get address"""

        return self._address

    def greet(self):
        """Used to greet"""

        print('Hello, my name is ' + self.Name +
              ' and I am ' + str(self.age) + ' years old')

    def set_age(self, new_age):
        """Used to set age"""
        
        if new_age > 0:
            self.age = new_age
        else:
            print('Age cannot be negative or zero.')

    def calculate_years_until_100(self):
        years_left = 100 - self.age
        return years_left
