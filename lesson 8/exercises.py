"""
Definisci una classe che rappresenta un libro.
La classe ha gli attributi di istanza
titolo, autore, anno pubblicazione e prezzo.
La classe ha anche un metodo che stampa,
con un messaggio a piacere, tutti i propri attributi.
Una volta completata la classe,
instanziane due oggetti, passando un argomento
per ciascun attributo di istanza.
Chiama su ciascuno dei due oggetti il metodo,
e verifica che il messaggio stampato sia corretto.
"""

class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def print_attributes(self):
        for attr in (self.title, self.author, self.year, self.price):
            print(attr)

lotr = Book("Lord Of The Rings", "J.R.R Tolkien", 1954, 40)
hp = Book("Harry Potter", "J.K Rowling", 1997, 30)

lotr.print_attributes()
hp.print_attributes()

'''
Alla classe dell'esercizio precedente
aggiungi un nuovo metodo,
che servirà ad applicare uno sconto al libro.

Il metodo perciò, prevede un parametro
che rappresenta la percentuale da scontare
e, in base ad essa riduce il prezzo originario
(rappresentato dall'attributo di istanza).

Una volta chiamato il metodo su un oggetto,
controlla se il prezzo è stato aggiornato correttamente.
Per controprova, controlla anche che il prezzo,
sull'altro oggetto sia rimasto invariato.

P.S.
Per calcolare il prezzo scontato, si può usare la formula:
Prezzo Scontato = Prezzo Originale x (100 - Percentuale) / 100
Ad esempio se il Prezzo Originale è 15.9
e passo come Percentuale di sconto 30
il prezzo finale dev'essere pari a 11.13.

'''

class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def print_attributes(self):
        print(f"Il libro {self.title} di {self.author}, pubblicato nel {self.year} ha un prezzo di {self.price}")
              
    def discount_price(self, percentage):
        discount = (100-percentage)/100
        self.price *= discount

lotr = Book("Lord Of The Rings", "J.R.R Tolkien", 1954, 40)
hp = Book("Harry Potter", "J.K Rowling", 1997, 30)

lotr.print_attributes()
hp.print_attributes()
lotr.discount_price(20)
hp.discount_price(20)
lotr.print_attributes()
hp.print_attributes()