# 4. Dada una cadena de ADN generar su diccionario que tenga el primer
# y último elemento de la cadena e indique cuantas veces aparece la primera y última base de la cadena.
adn = input("Input: ")
dic = {}
adn_init = adn[0]  # El caracter inicial
adn_last = adn[-1]  # El caracter final

for letra in adn:
    if letra == adn_last or letra == adn_init:
        if letra in dic:
            dic[letra] = dic[letra]+1
        else:
            dic[letra] = 1

print(dic)



# x  = dict()
# x = {1: "uno",
#      2: "dos",
#      3: "uno"}
