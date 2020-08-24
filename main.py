notas = []

while True:
    nota_1 = input("ingrese la primera nota : ")
    
    notas.append(nota_1)

    nota_2 = input("ingrese la segunda nota : ")

    notas.append(nota_2)

    nota_3 = input("ingrese la tercera nota : ")

    notas.append(nota_3)

    nota_4 = input("ingrese la cuarta nota : ")

    notas.append(nota_4)

    nota_5 = input("ingrese la quinta nota : ")

    notas.append(nota_5)
    break
print(f"las notas son : {notas}")   

notas.sort() #notas ordenadas

print(f"la nota menor es : {notas [0]}") #indice 

print(f"la nota mayor es : {notas [4]}")


a = ((sum(int(i) for i in notas)) / 5)

print(f"el promedio final de las notas es : {a}")