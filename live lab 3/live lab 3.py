# List> collection of ordered elements

lista = [1,2,3,4,5,6,]
lunghezza = len(lista) #6

"""
Scrivi un programma che richieda all'utente di inserire una serie di numeri separati da spazi.
Il programma dovrà convertire l'input in una lista di numeri interi,
quindi sommare soltanto i numeri pari presenti e infine stampare il risultato.
"""

numeri_stringa = input("Inserisci una sequenza di numeri separati da spazi: ")
numeri = numeri_stringa.split()

somma = 0
for numero in numeri: # per ogni numero
    numero = int(numero) # lo convertiamo in intero

    # se il numero è pari (ovvero se diviso per 2 da' resto 0)
    if numero % 2 == 0:
        somma = somma + numero

print(f"La somma totale è: {somma}")
