people = {1: {'nombre': 'Juan', 'edad': '27', 'sexo': 'M'},
          2: {'nombre': 'Maria', 'edad': '22', 'sexo': 'F'},
          3: {'nombre': 'Maria', 'edad': '22', 'sexo': 'F', "curso": {
              "creditos": 4, "profesor": "Jorge"}
              }
          }

print(people[3]["curso"]["profesor"])
