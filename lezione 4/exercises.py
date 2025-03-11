"""Scrivi un programma che richiede all'utente
il suo anno di nascita.
Usalo l'anno di nascita per calcolare l'età dell'utente.
Infine, stampa l'età dell'utente a schermo.
"""
CURRENT_YEAR = 2025
birth_year = int(input("In che anno sei nato?\n"))
age = CURRENT_YEAR-birth_year
print(f"La tua età è di {age} anni\n")

##############

"""
All'esercizio precedente aggiungi una variabile booleana
che rappresenta se l'utente è maggiorenne.
Per assegnare una variabile controlla se l'utente ha un età maggiore o uguale a 18
infine, stampala sul terminale"""

is_adult = age >= 18
print(is_adult)

##############
"""
All'esercizio precedente aggiungi una variabile booleana,
che rappresenta se l'utente ha la patente di guida, e che ha valore falso,
ora controlla se l'utente è maggiorenne e se possiede la patente,
salva tale informazione su una nuova variabile e poi stampala a schermo"""
import random
has_license = bool(random.randint(0, 1))
can_drive = has_license and is_adult
print(can_drive)
print("9.1".isdigit(), "aaaa")
####

