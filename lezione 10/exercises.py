'''
Crea una classe che rappresenta una persona,
e possiede gli attributi di istanza nome e età.
Ora crea una classe che rappresenta un regista,
che eredita dalla classe persona,
e possiede un attributo di istanza in più
che indica un film famoso che ha girato.

Istanzia un oggetto della superclasse,
poi un oggetto della sottoclasse,
e verifica quali attributi
sono accessibili su di essi.
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_attributes(self):
        for key in self.__dict__:
            print(self.__dict__[key])
class Director(Person):
    def __init__(self, name, age, film):
        super().__init__(name, age)
        self.film = film

    def show_attributes(self):
        print(self.film)

mario = Person("Mario", 30)
peter_jackson = Director("Peter", 63, "Lord of the Rings")

for obj in (mario, peter_jackson):
    print(type(obj).__name__, obj.__dict__)
    obj.show_attributes()


""""
"Alle classi dell'esercizio precedente,
aggiungi un metodo.
La classe Persona dovrà avere un metodo
che le permetta di presentarsi,
stampando a schermo i valori dei propri attributi.
La sottoclasse dovrà fare
un override di tale metodo,
per stampare a schermo un messaggio diverso,
che contenga il valore del suo
attributo specifico (film famoso).
"""