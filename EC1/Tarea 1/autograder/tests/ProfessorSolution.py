import sys
sys.setrecursionlimit(20000)

# SUS FUNCIONES EMPIEZA AQUI

def merge(left, right):
    i = j = 0
    merged_dicts = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_dicts.append(left[i])
            i += 1
        else:
            merged_dicts.append(right[j])
            j += 1

    while i < len(left):
        merged_dicts.append(left[i])
        i += 1

    while j < len(right):
        merged_dicts.append(right[j])
        j += 1

    return merged_dicts

def merge_sort(lista):
    if len(lista) == 1:
        return lista
    #mid = math.floor(len(dic) / 2)
    mid = len(lista) // 2
    i = 0
    ms_left = merge_sort(lista[:mid])
    ms_right = merge_sort(lista[mid:])
    return merge(ms_left, ms_right)


#
# def merge(left, right):
#     i = j = 0
#     merged_dicts = {}
#     left_arr = [[key, value] for key, value in left.items()]
#     right_arr = [[key, value] for key, value in right.items()]
#
#     while i < len(left) and j < len(right):
#         if left_arr[i][1] <= right_arr[j][1]:
#             merged_dicts[left_arr[i][0]] = left_arr[i][1]
#             i += 1
#         else:
#             merged_dicts[right_arr[j][0]] = right_arr[j][1]
#             j += 1
#
#     while i < len(left):
#         merged_dicts[left_arr[i][0]] = left_arr[i][1]
#         i += 1
#
#     while j < len(right):
#         merged_dicts[right_arr[j][0]] = right_arr[j][1]
#         j += 1
#
#     return merged_dicts
#
# def merge_sort(dic):
#     if len(dic) == 1:
#         return dic
#     #mid = math.floor(len(dic) / 2)
#     mid = len(dic) // 2
#     i = 0
#     left = {}
#     right = {}
#     for key, value in dic.items():
#         if i < mid:
#             left[key] = value
#         else:
#             right[key] = value
#         i += 1
#     ms_left = merge_sort(left)
#     ms_right = merge_sort(right)
#     return merge(ms_left, ms_right)

# SU FUNCIONES TERMINA AQUI

class ProfessorSolution:

    # NO MODIFICAR ABAJO DE ESTÁ LINEA, ES PARTE DEL AUTOGRADER
    def sort(self, data=[]):
        return "clear"

    def sorted(self, data=[]):
        return "clear"
    # NO MODIFICAR ARRIBA DE ESTÁ LINEA, ES PARTE DEL AUTOGRADER

    def crear_diccionarios(self, ruta="pokemon.csv"):
        pokemones = {}
        # SU SOLUCION EMPIEZA AQUI
        data = open(ruta, "r")
        l = 0
        for line in data:
            line_data = line.split(";")
            #print(line_data)
            pokemon={}
            if l > 0:
                pokemon["nombre"] = str(line_data[0])
                pokemon["puntos_ataque"] = int(line_data[2])
                pokemon["puntos_defensa"] = int(line_data[3])
                pokemon["puntos_velocidad"] = int(line_data[4])
                pokemon["habilidad"] =line_data[5].split('\n')[0]
                pokemones[int(line_data[1])] = pokemon

            l+=1
        data.close()

        # SU SOLUCION TERMINA AQUI
        return pokemones

    def buscar_dato_pokemon(self, pokemones, id, valor="habilidad"):
        result = ""
        # SU SOLUCION EMPIEZA AQUI
        # print(puntos_velocidad)
        pokemon = pokemones.get(id)
        result = pokemon[valor] if pokemon else "Pokémon no encontrado"
        #result = pokemones[id][valor]
        # print("buscar_dato_pokemon", result)
        # SU SOLUCION TERMINA AQUI
        return result

    def pokemon_rapido(self, pokemones):
        result = ()
        # SU SOLUCION EMPIEZA AQUI
        #puntos_velocidad = self.puntos_velocidad
        # print(puntos_velocidad)
        id_pokedex = -1
        max_velocidad = 0
        for key, value in pokemones.items():
            if value["puntos_velocidad"] > max_velocidad:
                max_velocidad = value["puntos_velocidad"]
                id_pokedex = key
        #result[pokemones[id_pokedex]["nombre"]] = pokemones[id_pokedex]["puntos_velocidad"]
        result = (pokemones[id_pokedex]["nombre"], pokemones[id_pokedex]["puntos_velocidad"])
        print("pokemon_rapido", result)
        # SU SOLUCION TERMINA AQUI
        return result

    def nombre_ascendente(self, pokemones):
        result = []
        # SU SOLUCION EMPIEZA AQUI
        #puntos_ataque = self.puntos_ataque
        # print(puntos_ataque)
        #puntos_ataque = {}
        #%for key, value in pokemones.items():
        #    puntos_ataque[key] = value["puntos_ataque"]
        #result = merge_sort_dict_descending_order(puntos_ataque)

        # nombres = {}
        # for key, value in pokemones.items():
        #     nombres[key] = value["nombre"]

        nombres = []
        for key, value in pokemones.items():
            nombres.append((value["nombre"], key))


        #result = merge_sort(nombres)

        result = merge_sort(nombres)

        # for key, value in nombres_ord.items():
        #     result.append((value, key))

        # print("nombre_ascendente", result)
        # f = open("testo.csv", "a")
        # f.write(str(result))
        # f.close()
        # SU SOLUCION TERMINA AQUI
        return result

    def busqueda_habilidad(self, nombre_a_buscar, nombres_ordenados, pokemones):
        result = {}
        # SU SOLUCION EMPIEZA AQUI
        # print(nombre_a_buscar)
        result = {-1: "No encontrado"}
        # nombres = {}
        # for key, value in pokemones.items():
        #     nombres[key] = value["nombre"]
        # nombres_ord = merge_sort(nombres)
        #
        # #print(nombres_ord)

        #nombres_ord = self.nombre_ascendente(pokemones)
        nombres_ord = nombres_ordenados
        # print(nombres_ord)

        izquierda = 0
        derecha = len(nombres_ord) - 1
        lista_pokemon = []

        # for key, value in nombres_ord.items():
        #     lista_pokemon.append([value, key])

        for item in nombres_ord:
            lista_pokemon.append([item[0], item[1]])

        while (izquierda <= derecha):
            medio = (izquierda + derecha) // 2
            nombre_pokemon = lista_pokemon[medio][0]
            if nombre_a_buscar > nombre_pokemon:
                izquierda = medio + 1
            elif nombre_a_buscar < nombre_pokemon:
                derecha = medio - 1
            else:
                pokemon = lista_pokemon[medio][1]
                result = {pokemon: pokemones[pokemon]}
                break

        print("busqueda_habilidad", result)
        # SU SOLUCION TERMINA AQUI
        return result