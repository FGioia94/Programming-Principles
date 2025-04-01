"""
Modifica l'esercizio della lezione precedente,
ma basandolo su un dizionario, invece che su una lista.
Il dizionario iniziale deve contenere
come chiave il prodotto da acquistare
e come valore la sua quantità.
All'utente sarà richiesto di inserire
sia il prodotto che la quantità.
Non è necessario ordinare il dizionario.
# """
def main():
    shopping_list = {"fagioli" : 2, 
            "noci" : 4, 
            "mele" : 3,}

    traverse_shopping_list(shopping_list)
    add_item(shopping_list)


def traverse_shopping_list(shopping_list):
    for item, amount in shopping_list.items():
        print(amount, item)

    
def add_item(shopping_list):
    user_item = input("Aggiungi un articolo: ").lower().strip()
    if not user_item:
        print("Errore: Non hai inserito alcun articolo")
    elif user_item in shopping_list:
        print("Errore: Articolo già presente")
    else:
        
        amount = input(f"Che quantità di {user_item} vuoi comprare?")
        if not amount.isdigit():
            amount = 1
        else:
            amount = int(amount)
        shopping_list[user_item] = amount
        print("Articolo aggiunto ✅")

    traverse_shopping_list(shopping_list)
    another = input("Scrivi Y se vuoi aggiungere un altro elemento")
    if another == "Y":
        add_item(shopping_list)
    
main()

"""
Definisci due dizionari che rappresentano una persona,
avente il campo nome, ed altri dati a piacere.
Entrambi i dizionari possiedono il campo età
ma non è valorizzato.
Definisci una funzione che prende in input dall'utente
l'anno di nascita,
calcola l'età e la restituisce.
Nel messaggio di input va stampato il nome della persona,
bisogna perciò passarlo alla funzione come argomento.
Per calcolare l'età servirà l'anno attuale,
che deve esser passato anch'esso alla funzione.
Infine, chiama due volte la funzione,
per valorizzare il campo età sui due dizionari. "
"""

person1 = {"name" : "Alice",
           "surname" : "Floris",
           "age": None,
           }

person2 = {"name" : "Franco",
           "surname" : "Puddu",
           "age": None,
           }

def main():
    for person in (person1, person2):
        person["age"] = ask_year(person)
        print(person)

def ask_year(person):
    birth_year = input(f"Hi {person["name"]}, please input your birth year:\n")
    if not birth_year.isdigit():
        return ask_year(person)
    else:
        return calculate_age(int(birth_year))

def calculate_age(birth_year):
    current_year = 2025
    return current_year - birth_year
main()
