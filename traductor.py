nombre = input ("escribe tu nombre " )
print (" --------Selecciona una opción---")
print (nombre + " presiona 1 para traductor de colores: inglés a español")
print (nombre + " presiona 2 para traductor de animales: español a inglés")
print (nombre + "presiona 3 para traductor de numeros: español a ingles")
print (nombre + "presiona 4 para traductor de partes del cuerpo inglés a español")
print (nombre + "presiona 5 para traductor de frutas: español a inglés")
opcion = int(input("escribe la opción que deseas utilizar del 1 al 5"))
if opcion == 1:
    print ("<<traductor de colores de inglés a español>>")
    op1 = input("¿Cual es el color que deseas pasar a español?")
    if op1 == "magenta":
        print("el color es magenta")
    elif op1 == "brown":
        print("el color es cafe")
    elif op1 == "Hazel":
        print ("el color es avellana")
    elif op1 == "pink":
        print("el color es rosa")
    elif op1 == "purple":
        print("el color es morado")
    elif op1 == "white":
        print("el color es el blanco")
    elif op1 == "gray":
        print("el color es gris")
    elif op1 == "green":
        print("el color es verde")
    elif op1 == "blue":
        print("el color es azul")
    elif op1 == "violet":
        print("el color es violeta")
if opcion == 2:
    print (">>traductor de animales de español a inglés<<")
    op2 = input("¿Cuál es el animal que deseas traducir al inglés?")
    if op2 == "ciervo":
        print ("deer")
    elif op2 == "oso":
        print ("bear")
    elif op2 == "caiman":
        print ("caiman")
    elif op2 == "puma":
        print ("cougar")
    elif op2 == "mono":
        print ("monkey")
    elif op2 == "pájaro":
        print ("bird")
    elif op2 == "cuervo":
        print == ("raven")
    elif op2 == "tiburon":
        print == ("shark")
    elif op2 == "araña":
        print == ("spider")
    elif op2 == "libelula":
        print ("dragonfly")
if opcion == 3:
    print ("----traductor de numeros español a inglés--")
    op3 = input("¿cual es tu numero que deseas traducir?")
    if op3 == "uno":
        print ("one")
    elif op3 == "dos":
        print ("two")
    elif op3 == "tres":
        print ("three")
    elif op3 == "cuatro":
        print ("four")
    elif op3 == "cinco":
        print ("five")
    elif op3 == "seis":
        print ("six")
    elif op3 == "siete":
        print ("seven")
    elif op3 == "ocho":
        print ("eight")
    elif op3 == "nueve":
        print ("nine")
    elif op3 == "diez":
        print ("ten")
if opcion == 4:
    print ("----traductor de partes del cuerpo inglés a español--")
    op4 = input("¿cual es la parte del cuerpo que deseas traducir? ")
    if op4 == "hand":
        print ("mano")
    elif op4 == "neck":
        print("cuello")
    elif op4 == "wrist":
        print("muñeca")
    elif op4 == "cabeza":
        print ("head")
    elif op4 == "muslo":
        print ("thigh")
    elif op4 == "thumb":
        print ("pulgar")
    elif op4 == "skin":
        print ("piel")
    elif op4 == "chin":
        print ("barbilla")
    elif op4 == "eyelid":
        print ("parpado")
    elif op4 == "forehead":
        print ("frente")
if opcion == 5:
    print ("----traductor de frutas de español a inglés--")
    op5 = input("¿cual es tu numero que deseas traducir? ")
    if op5 == "manzana":
        print ("apple")
    elif op5 == "cereza":
        print ("cherry")
    elif op5 == "fresa":
        print ("strawberry")
    elif op5 == "piña":
        print ("pineapple")
    elif op5 == "coco":
        print ("coconut")
    elif op5 == "limón":
        print ("lemon")
    elif op5 == "platano":
        print ("banana")
    elif op5 == "naranja":
        print ("orange")
    elif op5 == "mora azul":
        print ("blueberry")
    elif op5 == "kiwi":
        print ("kiwi")
else: 
        print ("su palabra no se encuentra en la base de datos.")