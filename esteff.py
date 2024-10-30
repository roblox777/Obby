print("Bienvenido a banco de México")
nombre = input("¿Cuál es tu nombre? ")
saldo = int(input("Ingresa tu saldo: "))
pin = input("Ingresa tu pin: ")

if pin == "2511":
    ejecutar = True

    while ejecutar:
        print("selecciona una opcion")
        print(nombre + " ¿Que operacion deseas hacer? tu saldo es de", saldo, "mxn")
        print("Presiona 1 para hacer un retiro")
        print("Presiona 2 para hacer un abono")
        print("Presiona 3 para checar tu saldo")
        op = int(input("Escribe la opción que deseas usar: "))
        
        if op == 1:
            retiro = int(input("escribe la cantidad que deseas retirar: "))
            if retiro > saldo:
                print("No tienes suficiente saldo para realizar esta operacion.")
            else:
                saldo -= retiro
                print("Tu saldo por el momento es de:", saldo, "mxn")
        
        elif op == 2:
            abono = int(input("escribe la cantidad que deseas abonar: "))
            saldo += abono
            print("Gracias por abonar a nuestra cuenta")
            print("Tu saldo ahora es de:", saldo, "mxn")
        elif op == 3:
            print("Tu saldo es de:", saldo, "mxn")
        
        else:
            print("Opcion no valida. Por favor intenta de nuevo.")
        
        r = input("Deseas hacer una nueva operacion? ")
        if r.lower() != "si":
            ejecutar = False