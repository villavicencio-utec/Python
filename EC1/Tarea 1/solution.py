import sys

sys.setrecursionlimit(20000)


# FUNCIONES RECURSIVAS EMPIEZAN AQUI

def merge(left, right):
    merged_list = []
    # SU SOLUCION EMPIEZA AQUI
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] > right[j]:
            merged_list.append(right[j])
            j += 1

        else:
            merged_list.append(left[i])
            i += 1

    while i != len(left):
        merged_list.extend(left[i:])

    while j != len(right):
        merged_list.extend(right[j:])

    # SU SOLUCION TERMINA AQUI
    return merged_list


def merge_sort(lista):
    # SU SOLUCION EMPIEZA AQUI
    left = ()  # debe implementar el valor correcto de left
    right = ()  # debe implementar el valor correcto de right

    listaID = []
    if len(lista) == 1:
        return lista
    if len(lista) > 1:
        left = lista[:len(lista) // 2]
        right = lista[len(lista) // 2:]

        leftID = listaID[:len(lista) // 2]
        rightID = listaID[len(lista) // 2:]
        merge_sort(left)
        merge_sort(right)

    # SU SOLUCION TERMINA AQUI
    return merge(left, right)


# FUNCIONES RECURSIVAS TERMINAN AQUI

class Solution:

    # NO MODIFICAR ABAJO DE ESTÁ LINEA, ES PARTE DEL AUTOGRADER
    def sort(self, data=[]):
        return "clear"

    def sorted(self, data=[]):
        return "clear"

    # NO MODIFICAR ARRIBA DE ESTÁ LINEA, ES PARTE DEL AUTOGRADER

    # ============ Pregunta  1============

    def crear_diccionarios(self, ruta="pokemon.csv"):
        pokemones = {}
        # SU SOLUCION EMPIEZA AQUI

        ruta = open(ruta, "r")
        primera_linea = True

        for linea in ruta:
            if not primera_linea:
                pokemon = linea.strip().split(";")
                diccionario_de_pokemones = {"nombre": pokemon[0], "puntos_ataque": int(pokemon[1]),
                                            "puntod_defensa": int(pokemon[2]), "puntos_velocidad": int(pokemon[3]),
                                            "habilidad": pokemon[4]}
                pokemones[id] = diccionario_de_pokemones

        ruta.close()
        # SU SOLUCION TERMINA AQUI
        return pokemones

    # ============ Pregunta  2============
    def buscar_dato_pokemon(self, pokemones, id, valor):
        result = ""
        # SU SOLUCION EMPIEZA AQUI

        if id in pokemones:
            respuesta = pokemones[id][valor]

        else:
            print('No se encontro al pokemon')

        # SU SOLUCION TERMINA AQUI
        return result

    # ============ Pregunta 3============
    def pokemon_rapido(self, pokemones):
        result = ()
        # SU SOLUCION EMPIEZA AQUI

        mayor = 0
        nombreDelMayor = ''
        for id in pokemones:
            if pokemones[id]['puntos_velocidad'] > mayor:
                mayor = pokemones[id]['puntos_velocidad']
                nombreDelMayor = pokemones[id]['nombre']

        # respuesta = (nombreDelMayor, mayor)

        # SU SOLUCION TERMINA AQUI
        return result

    # ============ Pregunta 4============
    def nombre_ascendente(self, pokemones):
        result = []
        # SU SOLUCION EMPIEZA AQUI

        for clave, valor in pokemones.items():
            result.append((valor["nombre"], clave))
        result = merge_sort(result)

        # SU SOLUCION TERMINA AQUI
        return result

    # ============ Pregunta 5============
    def busqueda_habilidad(self, nombre_a_buscar, nombres_ordenados, pokemones):
        result = {}
        # SU SOLUCION EMPIEZA AQUI

        # SU SOLUCION TERMINA AQUI
        return result