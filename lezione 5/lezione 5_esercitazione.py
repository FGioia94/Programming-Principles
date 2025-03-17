"""
Salva un numero a piacere su una variabile,
poi chiedi all'utente di indovinarlo

il numero deve essere da 0 a 9
Controlla se l'utento lo indovina, lo sbaglia o se inserisce un 
elemento fuori range e stampa a schermo un messaggio opportuno"""

number = 7

user_number = int(input("Specifica un numero da 0 a 9\n"))

if user_number == number:
    print("Indovinato!")
elif user_number <= 9 and user_number >= 0:
    print("Sbagliato, prova ancora\n")
else:
    print("Numero fuori range, prova ancora\n") 






