'''
Crea una lista della spesa che contenga
alcuni articoli a piacere.
Ordina gli articoli "alfabeticamente"
e poi stampali tutti a schermo,
ognuno di essi preceduto da un trattino.

Ora chiedi all'utente un nuovo articolo
da aggiungere.
Se l'utente non inserisce nulla,
stampa un messaggio di errore,
Se l'utente inserisce un articolo già presente,
stampa un messaggio di errore.
Se l'utente inserisce correttamente
un nuovo articolo,
aggiungilo alla lista.
In ogni caso, al termine del programma,
stampa nuovamente tutti gli articoli
(sempre ordinati alfabeticamente).
BONUS: attenzione al case!
'''

shopping_list = ["Bread", "Tomatoes", "Pasta", "Cheese"]
shopping_list.sort()
for obj in shopping_list:
    print("-", obj)

new_article = input("Add another article\n").title().strip
if not new_article:
    raise ValueError("Please input something\n")
elif new_article in shopping_list:
    raise ValueError("This item is already in the list\n")
else:
    shopping_list.append(new_article)
shopping_list.sort()
for obj in shopping_list:
    print("-", obj)


'''
Modifica il programma precedente:
se l'utente inserisce un articolo già presente,
chiedi all'utente se vuole rimuoverlo.
In caso affermativo, procedi alla rimozione.
'''

items = ["fagioli", "noci", "mele"]
items.sort()

for item in items:
    print("-", item)

user_item = input("Aggiungi un articolo: ").lower().strip()
if not user_item:
    print("Errore: Non hai inserito alcun articolo")
elif user_item in items:
    print("Errore: Articolo già presente")
else:
    if user_item in items:
        ask_remove = input("Articolo già presente, scrivi \"Y\" se vuoi rimuoverlo\n")
        if ask_remove == "Y":
            items.remove(user_item)
    else:
        items.append(user_item)
        print("Articolo aggiunto ✅")
        items.sort()

for item in items:
    print("-", item)
