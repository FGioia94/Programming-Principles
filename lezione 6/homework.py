'''
Modifica il programma precedente:
l'utente deve poter inserire più articoli alla volta,
separandoli col carattere |
In tal caso, il programma converte
tale stringa inserita dall'utente in una lista di articoli,
i quali vengono poi aggiunti alla lista iniziale.
Per semplicità, non controllare se l'utente
inserisce articoli già presenti o stringhe vuote.
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
    user_answer = input("Vuoi rimuoverlo? In caso affermativo scrivi si: ").lower().strip()
    if user_answer == "si":
        items.remove(user_item)
        print("Articolo rimosso")
    else:
        print("Articolo non rimosso")
        
elif "|" in user_item:
    user_item = user_item.split("|")
    items.extend(user_item)
else:
    items.append(user_item)
    
print("Articolo aggiunto ✅")
items.sort()

print("LISTA MODIFICATA")
for item in items:
    print("-", item)