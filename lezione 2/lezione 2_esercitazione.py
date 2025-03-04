'''
Stampa sul terminale, uno sotto l'altro, 
i tre personaggi principali del film "Tre uomini e una gamba". 
Usa solo argomenti posizionali
'''

print("Aldo")
print("Giovanni")
print("Giacomo")

# other solution
print("Aldo\nGiovanni\nGiacomo")

###################################################
'''
Ora aggiungi alle print precedenti 
uno o più argomenti keyword affinchè la stampa divenga come segue
Aldo,Giovanni,Giacomo.'''

print("Aldo", "Giovanni", "Giacomo.", sep = ",")

# other solution
print("Aldo", end = ",")
print("Giovanni", end = ",")
print("Giacomo", end = ".")
# other solution

print("Aldo", "Giovanni", "Giacomo", sep = ",", end = ".")

###################################################

'''
Stampa il testo seguente, usando una sola funzione print
Jacqueline>Marge>Lisa
Gli argomenti posizionali non devono contenere il carattere >'''

print("Jacqueline", "Marge", "Lisa", sep = ">")
# other solution

print("Jacqueline", end = ">")
print("Marge", end = ">")
print("Lisa")

###################################################

'''
Genera almeno 4 errori di sintassi e 4 di runtime
'''
# syntax error
# print("a"
# print a
# print a"
# print("a","b", end ",")

# runtime error
# print("test", a)
# input("a", 1) #TypeError: input expected at most 1 argument, got 2
# print(start = True) #TypeError: print() got an unexpected keyword argument 'start'
# pippo() #NameError: name 'pippo' is not defined

###################################################

'''
Chiedi all'utente il proprio nome, 
fai si che possa inserirlo nel terminale, 
catturalo e stampalo a schermo con un testo simile

Nome Utente = Edo
'''

name = input("Come ti chiami?\n")
print("Nome Utente =", name)

# other solution
name = input("Come ti chiami?\n")
print("Nome Utente", name, sep = " = ")

###################################################
'''
Fai la stessa cosa ma senza usare variabili'''
print("Nome Utente =", input("Come ti chiami?\n"))
# other solution
print("Nome Utente", input("Come ti chiami?\n"), sep = " = ")

