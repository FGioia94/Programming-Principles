telephone_number = "4444444444"
is_iphone = False
telephone_price = 500
telephone_weight = 150.0

""" 
Scrivi un programma che definisce una variabile, 
poi ne modifica il valore, mantentnedo il modesimo data type, 
infine ne modifica il datatype
Stampa sulterminale la variabile e il suo tipo dopo ognuno dei tre passaggi """

my_var = 2
print(my_var, type(my_var))
my_var += 1
print(my_var, type(my_var))
my_var = "test"
print(my_var, type(my_var))

print(type(object))

"""
Richiedi un input all'utente, salvalo su una variabile
poi stampane il tipo sul terminale"""
val = input()
print(type(val))

"""
Homework:
Implementa il trova e sostituisci!
Richiedi all'utente quale parola vuole trovare
e con quale vuole sostituirla.
Applica tali sostituzioni ad un testo
Infine, stampa il testo modificato sul terminale. 
"""

BASE_TEXT = """Harry si sentì leggero mentre saliva sulla scopa volante.
Per la prima volta, Harry provò il brivido del decollo.
Quella del volo, diventò immediatamente la più grande passione di Harry."""

search_with = input("Type the word to search for\n")
replace_with = input("Type the word you want to replace with\n")
print(BASE_TEXT.replace(search_with, replace_with))
