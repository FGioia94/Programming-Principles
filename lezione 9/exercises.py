'''
Definisci una classe che rappresenti
uno strumento musicale,
ad esempio una chitarra, un piano, etc...
Assegna alla classe almeno due attributi d'istanza
e almeno due attributi di classe, a piacere.

Istanzia un oggetto della classe e applica
il principio della Instrospection:
con le funzioni hasattr e dir,
verifica quali attributi sono accessibili
sull'oggetto e quali sulla classe.
'''

'''
Alla classe dell'esercizio precedente,
aggiungi un attributo di istanza PRIVATO.
Verifica, sull'oggetto istanziato, che tale attributo
NON sia accessibile.
Una volta effettuata questa verifica,
aggiungi alla definizione della classe,
un metodo che permetta di restituire il valore
dell'attributo privato.

BONUS:
Aggiungi alla classe un altro metodo,
che permette di MODIFICARE l'attributo privato.
(il metodo prende un parametro in ingresso
e lo usa per valorizzare l'attributo privato)
'''


class Guitar:
    material = "wood"
    strings = 6

    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

        self.__guitarID = "abcde"

    def __str__(self):
        print(f"I am a {self.name} guitar")

    def get_id(self):
        return(self.__guitarID)
    def set_id(self, value):
        self.__guitarID = value
gibson = Guitar("Gibson", 1000, "red")
fender = Guitar("Fender", 700, "blue")

instance_attributes = gibson.__dir__()
class_attributes = []
for attr in instance_attributes:
    if hasattr(Guitar, attr):
        class_attributes.append(attr)
print(f"Class Attributes: {class_attributes}")
print(f"Instance Attributes: {instance_attributes}")
gibson.__str__()


try:
    print(fender.__guitarID())
except AttributeError:
    print("Attribute unreachable")

print(fender.get_id())
fender.set_id("12345")
print(fender.get_id())

