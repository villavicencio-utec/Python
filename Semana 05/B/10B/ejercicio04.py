# 4. Dada una cadena de ADN generar su diccionario que tenga el primer
# y último elemento de la cadena e indique cuantas veces aparece la primera y última base de la cadena.
adn = input("Input: ")
dic = {}
adn_init = adn[0]
adn_last = adn[-1]

for letra in adn:
    if letra == adn_last or letra == adn_init:
        if letra in dic:
            dic[letra] = dic[letra]+1
        else:
            dic[letra] = 1

print(dic)
