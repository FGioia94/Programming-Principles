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
import random
import time
class Pokemon:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(90, 130)
        self.strength = random.randint(6, 10)
    
    def attacks(self, target):
        multiplier = random.randint(1,4)
        if multiplier == 4:
            print("CRITICAL HIT \n")
        damage = self.strength * multiplier
        target.health -= damage
        print(f"{self.name} deals {damage} damage to {target.name}")

def main():
    starters = ["Charmander", "Squirtle", "Bulbasaur"]
    pokemon_1 = Pokemon(random.choice(starters))
    starters.remove(pokemon_1.name)
    pokemon_2 = Pokemon(random.choice(starters))

    print(f"{pokemon_1.name} VS {pokemon_2.name}\n")
    
    counter = 0
    while not pokemon_1.health <= 0 and not pokemon_2.health <= 0:
        attacker = pokemon_1 if counter%2 == 0 else pokemon_2
        
        defender = [p for p in [pokemon_1, pokemon_2] if p != attacker][0]
        if not counter == 0:
            print(f"{defender.name} has {defender.health} HP left\n")
        counter += 1
        print(f"{attacker.name}'s turn\n")
        time.sleep(2)
        print(f"{attacker.name} is attacking {defender.name}\n")
        time.sleep(2)
        attacker.attacks(defender)
        time.sleep(4)

    print(f"{defender.name} has 0 HP left, {attacker.name} wins!\n")

main()