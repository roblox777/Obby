print("Bienvenido a crumbl cookies 🍪🍪🍪")
ct = 0
while True:
    print("Escribe 1 para comprar galletas")
    print("Escribe 2 para comprar pasteles")
    op = int(input("Por favor, selecciona la opción de postre que deseas comprar: "))  

    if op == 1:
        print("----Has seleccionado las galletas.----")
        print("A continuación, se te mostrará el menú de galletas de nuestra tienda: ")
        print("1 = milk chocolate chip 52$")
        print("2 = mint chip ice cream 67$")
        print("3 = chocolate cake batter 72$")
        print("4 = cinnamon crunch 66$")
        print("5 = Olivia Rodrigo's GUTS cookie 96$")
        print("6 = Chocolate covered strawberry 77$")
        print("7 = Kentucky butter cake 81$")
        print("8 = Matcha covered cookie 85$")  
        while True:
            p = int(input("Ingresa el número de la galleta que quieres pedir: "))
            if p == 1:
                print("Has seleccionado la milk chocolate chip cookie")
                d = float(input("Ingresa la cantidad de galletas que quieres comprar: "))
                c = 52 * d
            elif p == 2:
                print("Has seleccionado la mint chip ice cream cookie")
                d = float(input("Ingresa la cantidad de galletas que quieres comprar: "))
                c = 67 * d
            elif p == 3:
                print("Has seleccionado la chocolate cake batter cookie")
                d = float(input("Ingresa la cantidad de galletas que quieres comprar: "))
                c = 72 * d
            elif p == 4:
                print("Has seleccionado la cinnamon crunch cookie")
                d = float(input("Ingresa la cantidad de galletas que quieres comprar: "))
                c = 66 * d
            elif p == 5:
                print("Has seleccionado la Olivia Rodrigo's GUTS cookie")
                d = float(input("Ingresa la cantidad de galletas que quieres comprar: "))
                c = 96 * d
            elif p == 6:
                print("Has seleccionado la Chocolate covered strawberry cookie")
                d = float(input("Ingresa la cantidad de galletas que quieres comprar: "))
                c = 77 * d
            elif p == 7:
                print("Has seleccionado la Kentucky butter cake cookie")
                d = float(input("Ingresa la cantidad de galletas que quieres comprar: "))
                c = 81 * d
            elif p == 8:
                print("Has seleccionado la Matcha covered cookie")
                d = float(input("Ingresa la cantidad de galletas que quieres comprar: "))
                c = 85 * d
            else:
                print("La opcion que has insertado no existe :((")
                continue
            ct = ct + c
            print("El costo sería de: ", c)
            otr = input("¿Deseas comprar algo mas?: ")
            if otr.lower() != "si":
                break

    elif op == 2:
        print("----Has seleccionado los pasteles.----")
        print("A continuación, se te mostrará el menú de pasteles de nuestra tienda: ")
        print("1 = Raspberry cheesecake 102$")
        print("2 = Pistachio Gelato 167$")
        print("3 = Blueberry muffin 122$")
        print("4 = Caramel praline 96$")
        
        while True:
            p = int(input("Ingresa el número del pastel que quieres pedir: "))
            if p == 1:
                print("Has seleccionado la Raspberry cheesecake")
                d = float(input("Ingresa la cantidad de pasteles que quieres comprar: "))
                c = 102 * d
            elif p == 2:
                print("Has seleccionado la Pistachio Gelato")
                d = float(input("Ingresa la cantidad de pasteles que quieres comprar: "))
                c = 167 * d
            elif p == 3:
                print("Has seleccionado la Blueberry muffin")
                d = float(input("Ingresa la cantidad de pasteles que quieres comprar: "))
                c = 122 * d
            elif p == 4:
                print("Has seleccionado la caramel praline")
                d = float(input("Ingresa la cantidad de pasteles que quieres comprar: "))
                c = 96 * d
            else:
                print("La opcion que has insertado no existe :((")
                continue
            ct = ct + c
            print("El costo seria de: ", c)
            otr = input("¿deseas comprar algo mas?: ")
            if otr.lower() != "si":
                break
    else:
        print("La opcion que has insertado no existe :((")
    
    continuar = input("¿Desea comprar algo mas?: ")
    if continuar.lower() != "si":
        break
print("¡gracias por su compra :)!")
print("el total de su compra es:", ct)
