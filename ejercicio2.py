print("Sistema para calcurar el promedio de un alumno")
nombre = input ("Para comemzar, ¿ Cuál es tu nombre?: ")
matematicas = int(input(nombre + " ¿Cuál es tu calificación de matemáticas?: "))
quimica = int(input(nombre + " ¿Cuál es tu calificacion de química?: "))
español = int(input(nombre + " ¿Cuál es tu calificación de español?:"))
ingles = int(input(nombre + " ¿Cuál es tu calificación de inglés?"))
historia = int (input(nombre + " ¿Cuál es tu calificación de historia?"))
computacion = int(input(nombre + " ¿Cuál es tu calificación de computación?"))
promedio = (matematicas + quimica + español + ingles + historia + computacion)/6
if promedio >= 60:
    print("felicidades " + nombre + " aprobaste con un promedio de:", promedio)
elif promedio >= 70 :
    print("¡Tu puedes!")
elif promedio >= 80 :
    print("¡Vas muy bien!")
elif promedio >=90 :
    print ("¡Felicidades! :)")
elif promedio >=100:
    print ("¡Excelente!")
else:
    print("reprobaste :(")
print("fin")