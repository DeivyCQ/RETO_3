alumnos = []
notas_alumno_1 = []
while True:
   x = input(f"ingrese los datos del estudiante : ")
   alumnos.append(x) 

   a = input(f"ingrese la primera nota : ")
   notas_alumno_1.append(a)

   a = input(f"ingrese la segunda nota : ")
   notas_alumno_1.append(a)

   a = input(f"ingrese la tercera nota : ")
   notas_alumno_1.append(a)

   a = input(f"ingrese la cuarta nota : ")
   notas_alumno_1.append(a)

   a = input(f"ingrese la cuarta nota : ")
   notas_alumno_1.append(a)

   print(f"las notas de {alumnos [0]} son : {notas_alumno_1}")
   notas_alumno_1.sort()

   print(f"la nota menor del alumno {alumnos [0]} es : {notas_alumno_1 [0]}")
   print(f"la nota mayor del alumno {alumnos [0]} es : {notas_alumno_1 [4]}")

   print(f"el promedio de las notas de {alumnos [0]} es : {(sum(int(i) for i in notas_alumno_1)) / 5}")
   break
print("#############################################")

notas_alumno_2 = []
while True:
   x = input(f"ingrese los datos del estudiante : ")
   alumnos.append(x) 

   a = input(f"ingrese la primera nota : ")
   notas_alumno_2.append(a)

   a = input(f"ingrese la segunda nota : ")
   notas_alumno_2.append(a)

   a = input(f"ingrese la tercera nota : ")
   notas_alumno_2.append(a)

   a = input(f"ingrese la cuarta nota : ")
   notas_alumno_2.append(a)

   a = input(f"ingrese la cuarta nota : ")
   notas_alumno_2.append(a)

   print(f"las notas de {alumnos [1]} son : {notas_alumno_1}")
   notas_alumno_2.sort()

   print(f"la nota menor del alumno {alumnos [1]} es : {notas_alumno_2 [0]}")
   print(f"la nota mayor del alumno {alumnos [1]} es : {notas_alumno_2 [4]}")

   print(f"el promedio de las notas de {alumnos [1]} es : {(sum(int(i) for i in notas_alumno_2)) / 5}")
   break
print("###################################################")

notas_alumno_3 = []
while True:
   x = input(f"ingrese los datos del estudiante : ")
   alumnos.append(x) 

   a = input(f"ingrese la primera nota : ")
   notas_alumno_3.append(a)

   a = input(f"ingrese la segunda nota : ")
   notas_alumno_3.append(a)

   a = input(f"ingrese la tercera nota : ")
   notas_alumno_3.append(a)

   a = input(f"ingrese la cuarta nota : ")
   notas_alumno_3.append(a)

   a = input(f"ingrese la cuarta nota : ")
   notas_alumno_3.append(a)

   print(f"las notas de {alumnos [2]} son : {notas_alumno_3}")
   notas_alumno_3.sort()

   print(f"la nota menor del alumno {alumnos [2]} es : {notas_alumno_3 [0]}")
   print(f"la nota mayor del alumno {alumnos [2]} es : {notas_alumno_3 [4]}")

   print(f"el promedio de las notas de {alumnos [2]} es : {(sum(int(i) for i in notas_alumno_3)) / 5}")
   break

print("##################################################")

print(f"los alumnos son : {alumnos}")