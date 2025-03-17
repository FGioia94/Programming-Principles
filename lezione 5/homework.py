'''
EX2: WHILE
Modifica il programma precedente per
continuare a chiedere il numero all'utente
finché non riesce ad indovinarlo
''' 

import random
number = random.randint(0, 9)

user_input = None
while user_input != number: 
    user_input = int(input("Specifica un numero da 0 a 9\n"))
    if 0<=user_input<=9:
        print("Sbagliato, prova ancora\n")
    else:
        print("Numero fuori range, prova ancora\n")
print("Indovinato!\n")

'''
EX3: FOR
Modifica il programma precedente per
implementare il numero di tentativi.
Stavolta è vietato utilizzare il ciclo while!
Ad ogni iterazione,
stampa il numero del tentativo corrente,
as esempio “Tentativo n. 1”
poi, come sempre, richiedi l'inserimento del numero,
e valuta se è corretto.
Se l'utente non indovina entro 5 tentativi,
il gioco termina, stampando un messaggio opportuno.
''' 

import random
number = random.randint(0, 9)
for i in range(5):
    user_input = int(input("Specifica un numero da 0 a 9\n"))
    if user_input == number:
        print("indovinato!")
        break
    else:
        if 0<=user_input<=9:
            print("Sbagliato, prova ancora\n")
        else:
            print("Numero fuori range, prova ancora\n")

        print(f"Ancora {4-i} Tentativi\n")
else:
    print("Hai perso!\n")