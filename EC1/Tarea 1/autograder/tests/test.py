import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility

import sys
sys.setrecursionlimit(20000)
from ProfessorSolution import ProfessorSolution
try:
    from solution import Solution
except Exception as e:
    raise Exception(f'No se pudo importar su clase Solution de "solution.py", por favor recordar trabajar a partir del template. El error es: {e}')



class TestSolution(unittest.TestCase):

    # Pregunta 1
    @weight(1.5)
    def test1(self):
        """Pregunta 1: creación de diccionario con set de datos 1"""
        data = open("test1.csv", "r")
        pokemonesSol = data.readline()
        data.close()
        stb = Solution()
        pokemones = stb.crear_diccionarios("pokemon1.csv")
        self.assertEqual(str(pokemones), pokemonesSol, f'Test fallido. Revisa la creación del diccionario')

    @weight(1.5)
    def test2(self):
        """Pregunta 1: creación de diccionario con set de datos 2"""
        data = open("test2.csv", "r")
        pokemonesSol = data.readline()
        data.close()
        stb = Solution()
        pokemones = stb.crear_diccionarios("pokemon2.csv")
        self.assertEqual(str(pokemones), pokemonesSol, f'Test fallido. Revisa la creación del diccionario')

    # Pregunta 2
    @weight(1)
    def test3(self):
        """Pregunta 2: Buscar dato de Pokémon inexistente con set de datos 1"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon1.csv")
        solution_result = stb.buscar_dato_pokemon(pokemonesSol, 20000,"habilidad")
        self.assertEqual(solution_result, "Pokémon no encontrado", f'Test fallido. No obtuviste el dato correcto, revisa el método buscar_dato_pokemon.')

    @weight(1)
    def test4(self):
        """Pregunta 2: Buscar dato de Pokémon con set de datos 1"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon1.csv")
        solution_result = stb.buscar_dato_pokemon(pokemonesSol,16425,"puntos_velocidad")
        self.assertEqual(solution_result, 60, f'Test fallido. No obtuviste el dato correcto, revisa el método buscar_dato_pokemon.')

    @weight(1)
    def test5(self):
        """Pregunta 2: Buscar dato de Pokémon con set de datos 2"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon2.csv")
        solution_result = stb.buscar_dato_pokemon(pokemonesSol, 5664,"puntos_ataque")
        self.assertEqual(solution_result, 120, f'Test fallido. No obtuviste el dato correcto, revisa el método buscar_dato_pokemon.')

    # Pregunta 3
    @weight(2)
    def test6(self):
        """Pregunta 3: Pokémon más rápido con set de datos 1"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon1.csv")
        solution_result = stb.pokemon_rapido(pokemonesSol)
        self.assertEqual(solution_result, ('Ninjask19', 183),f'Test fallido. No obtuviste el pokemon más rápido, revisa tu algoritmo de búsqueda.')

    @weight(2)
    def test7(self):
        """Pregunta 3: Pokémon más rápido con set de datos 2"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon2.csv")
        solution_result = stb.pokemon_rapido(pokemonesSol)
        self.assertEqual(solution_result, ('Deoxys23', 199),f'Test fallido. No obtuviste el pokemon más rápido, revisa tu algoritmo de búsqueda.')

    # Pregunta 4
    @weight(2.5)
    def test8(self):
        """Pregunta 4: Diccionario ordenado ascendentemente por nombre de Pokémon con set de datos 1"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        data = open("test8.csv", "r")
        resultado = data.readline().split("\n")[0]
        data.close()
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon1.csv")
        solution_result = stb.nombre_ascendente(pokemonesSol)
        self.assertEqual(str(solution_result), resultado,  f'Test fallido. No obtuviste los nombres en orden ascendente, revisa tu algoritmo de ordenamiento.')


    @weight(2.5)
    def test9(self):
        """Pregunta 4: Diccionario ordenado ascendentemente por nombre de Pokémon con set de datos 2"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        data = open("test9.csv", "r")
        resultado = data.readline().split("\n")[0]
        data.close()
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon2.csv")
        solution_result = stb.nombre_ascendente(pokemonesSol)
        self.assertEqual(str(solution_result), resultado, f'Test fallido. No obtuviste los nombres en orden ascendente, revisa tu algoritmo de ordenamiento.')

    # Pregunta 5
    @weight(2)
    def test10(self):
        """Pregunta 5: Búsqueda binaria con nombre de Pokémon, usando set de datos 1"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon1.csv")
        solution_result = stb.busqueda_habilidad("Squirtle1", prof.nombre_ascendente(pokemonesSol), pokemonesSol)
        self.assertEqual(solution_result, {7: {'nombre': 'Squirtle1', 'puntos_ataque': 50, 'puntos_defensa': 64, 'puntos_velocidad': 43, 'habilidad': 'Torrent'}}, f'Test fallido. No obtuviste la información del Pokémon Squirtle1, revisa tu algoritmo de búsqueda binaria.')

    @weight(1)
    def test11(self):
        """Pregunta 5: Búsqueda binaria con nombre de Pokémon inexistente, usando set de datos 1"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon2.csv")
        solution_result = stb.busqueda_habilidad("Charmeleon29", prof.nombre_ascendente(pokemonesSol), pokemonesSol)
        self.assertEqual(solution_result, {-1: 'No encontrado'}, f'Test fallido. El Pokémon Charmeleon29 no existe en el diccionario, revisa tu algoritmo de búsqueda binaria.')

    @weight(2)
    def test12(self):
        """Pregunta 5: Búsqueda binaria con nombre de Pokémon, usando set de datos 2"""
        stb = Solution()
        solution_result = stb.sort()
        self.assertEqual(solution_result, "clear", f'No modifique la función sort del template')
        solution_result = stb.sorted()
        self.assertEqual(solution_result, "clear", f'No modifique la función sorted del template')
        prof = ProfessorSolution()
        pokemonesSol = prof.crear_diccionarios("pokemon2.csv")
        solution_result = stb.busqueda_habilidad("Pikachu20", prof.nombre_ascendente(pokemonesSol), pokemonesSol)
        self.assertEqual(solution_result, {15225: {'nombre': 'Pikachu20', 'puntos_ataque': 50, 'puntos_defensa': 50, 'puntos_velocidad': 90, 'habilidad': 'Static'}}, f'Test fallido. No obtuviste la información del Pokémon Pikachu20, revisa tu algoritmo de búsqueda binaria.')


if __name__ == '__main__':
    unittest.main()
