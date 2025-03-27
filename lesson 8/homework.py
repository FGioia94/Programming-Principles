"""
Crea una classe Pokemon coi seguenti attributi:
Nome, Salute e Forza.
Implementa un metodo di attacco che permetta
a un Pokemon di attaccarne un altro,
riducendo la Salute dell'avversario.
(al metodo passeremo come argomento un oggetto Pokemon)
La Salute dell'avversario viene ridotta
di un valore pari alla Forza dell'attaccante.
Il metodo infine stampa un messaggio,
con alcuni dettagli sull'attacco, ad esempio:
Pikachu attacca Charizard causando 15 danni!

Completata la classe, istanzia due Pokemon
e falli attaccare l'un l'altro, quante volte desideri.
Dopo il combattimento, stampa la Salute
di entrambi, per vedere se è coerente con gli attacchi.
"""

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.