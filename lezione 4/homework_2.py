"""
Hai i seguenti numeri binari:
0b1011
0b0101
Utilizza fra loro un operatore bitwise,
affinché il risultato sia un numero binario
con tutti i bit settati ad 1,
eccetto l'ultimo bit (quello più a destra)
"""

bit_1 = 0b1011
bit_2 = 0b0101
bit3 = bit_1 ^ bit_2
print(bin(bit3))