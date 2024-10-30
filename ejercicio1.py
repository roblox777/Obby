nombre = (input("Escribe tu nombre por favor "))
print ("Hola,",nombre)
edad = int(input("¿Cuántos años tienes? "))
if edad <18:
    print ("Oh, no tienes permitido acceder a este contenido :(")
elif edad >18:
    print ("Cumples con el requisito de edad")
if edad >30:
    print ("Definitivamente puedes ver esta pelicula")
if edad <5:
    print ("¿Sabes leer?")
if edad >120:
    print ("Aunque con esa edad, asumo que eres un fósil")