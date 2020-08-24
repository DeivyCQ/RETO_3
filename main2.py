alumnos = ("Alberto", "Juan", "Daniel")
notas_de_Alberto = []
        # para Alberto      
while True:
    nota = input(f"ingrese la primera nota de {alumnos [0]} : ")
    notas_de_Alberto.append(nota)

    nota = input(f"ingrese la segunda nota de {alumnos [0]} : ")
    notas_de_Alberto.append(nota)

    nota = input(f"ingrese la tercera nota de {alumnos [0]} : ")
    notas_de_Alberto.append(nota)

    nota = input(f"ingrese la cuarta nota de {alumnos [0]} : ")
    notas_de_Alberto.append(nota)

    nota = input(f"ingrese la quinta nota de {alumnos [0]} : ")
    notas_de_Alberto.append(nota)

    print(f"las notas de {alumnos [0]} son: {notas_de_Alberto} ")

    notas_de_Alberto.sort()

    print(f"La nota menor de {alumnos [0]} es : {notas_de_Alberto [0]}")
    print(f"La nota mayor de {alumnos [0]} es : {notas_de_Alberto [4]}")



    print(f"el promedio de las notas de {alumnos [0]} es : {(sum(int(i) for i in notas_de_Alberto)) / 5}")

    break
print("#######################################################")
notas_de_Juan = []

while True:
    nota = input(f"ingrese la primera nota de {alumnos [1]} : ")
    notas_de_Juan.append(nota)

    nota = input(f"ingrese la segunda nota de {alumnos [1]} : ")
    notas_de_Juan.append(nota)
    
    nota = input(f"ingrese la tercera nota de {alumnos [1]} : ")
    notas_de_Juan.append(nota)

    nota = input(f"ingrese la cuarta nota de {alumnos [1]} : ")
    notas_de_Juan.append(nota)

    nota = input(f"ingrese la quinta nota de {alumnos [1]} : ")
    notas_de_Juan.append(nota)

    print(f"Las notas de {alumnos [1]} son : {notas_de_Juan}")
    notas_de_Juan.sort()

    print(f"la nota menor es : {notas_de_Juan [0]}")
    print(f"la nota mayor es : {notas_de_Juan [4]}")

    print(f"el promedio de las notas de {alumnos [1]} es : {(sum(int(i) for i in notas_de_Juan)) / 5}")
    break
print("########################################################")
notas_de_Daniel = []

while True:
    nota = input(f"ingresa la primera nota de {alumnos [2]} : ")
    notas_de_Daniel.append(nota)

    nota = input(f"ingresa la segunda nota de {alumnos [2]} : ")
    notas_de_Daniel.append(nota)

    nota = input(f"ingresa la tercera nota de {alumnos [2]} : ")
    notas_de_Daniel.append(nota)

    nota = input(f"ingresa la cuarta nota de {alumnos [2]} : ")
    notas_de_Daniel.append(nota)

    nota = input(f"ingresa la quinta nota de {alumnos [2]} : ")
    notas_de_Daniel.append(nota)

    print(f"las notas de {alumnos [2]} son : {notas_de_Daniel}")
    notas_de_Daniel.sort()

    print(f"la nota menor es : {notas_de_Daniel [0]}")
    print(f"la nota mayor es : {notas_de_Daniel [4]}")

    print(f"el promedio de las notas de {alumnos [1]} es : {(sum(int(i) for i in notas_de_Daniel)) / 5}")
    break