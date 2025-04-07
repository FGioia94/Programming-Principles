"""
Definisci una lista che contenga 3 mete turistiche
Stampale tutte a schermo e chiedi all'utente 
dove desidera andare.
Per scegliere, dovrà immettere
l'indice dell'elemento della lista,
In questo caso un numero da 0 a 2.
Stampa a schermo un augurio di buon viaggio,
contenente la destinazione scelta

Lancia il programma e tenta di farlo andare in errore,
così da trovare le eccezioni che potrebbero
verificarsi nel processo
"""

destinations = ["Rome", "Paris", "London"]

print(f"Available destinations are: {destinations}")

try:
    index = int(input("Please type the index of your destination\n"))
    if index < 0:
        raise(IndexError)
except ValueError:
    print("Your index should be an integer")
except IndexError:
    print(f"Your index should be from 0 to {len(destinations) - 1}")
except Exception as e:
   print("Error: ", e)

else:
    print(f"Have a great trip to {destinations[index]}")