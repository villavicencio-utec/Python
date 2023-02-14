# Escriba un programa que permita registrar una lista de cursos en un archivo 2.JSON.
# El curso debe tener los siguientes campos:  nombre, carrera, ciclo, créditos, docente.
# El campo “docente” es también un diccionario que contiene los siguientes campos: nombre, correo y horario_oficina.

import json
# un objeto de tipo Diccionario:

obj = {
    1:{
        "nombre": "Programacion I",
        "carrera": "Computer Science",
        "ciclo": 5,
        "creditos": 4,
        "docente": {
            "nombre": "Jorge Villavicencio",
            "correo": "jvillavicencio@utec.edu.pe",
            "horario_oficina": "6:00-8:00 pm",
        }
    },
        2: {
            "nombre": "Programacion II",
            "carrera": "Computer Science",
            "ciclo": 5,
            "creditos": 4,
            "docente": {
                "nombre": "Jorge Villavicencio",
                "correo": "jvillavicencio@utec.edu.pe",
                "horario_oficina": "6:00-8:00 pm",
            }
        },

            3: {
                "nombre": "Inteligencia artificial",
                "carrera": "Computer Science",
                "ciclo": 5,
                "creditos": 4,
                "docente": {
                    "nombre": "Jorge Villavicencio",
                    "correo": "jvillavicencio@utec.edu.pe",
                    "horario_oficina": "6:00-8:00 pm",
                }
            }
  }

# guardar en un archivo 2.JSON:
with open('ejercicio_1.json', 'w') as outfile: # w write , r read
  # convertir a 2.JSON:
  json.dump(obj, outfile)


