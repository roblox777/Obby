def mostrar_menu():
    print("Bienvenido a Crumbl Cookies 🍪")
    print ("1 = Milk Chocolate Chip - $52")
    print ("2 = Mint Chip Ice Cream - $67")
    print ("3 = chocolate cake batter 72$")
    print ("4 = cinnamon crunch 66$")
    print ("5 = Olivia Rodrigo's GUTS cookie 96$")
    print ("6 = Chocolate covered strawberry 77$")
    print ("7 = Kentucky butter cake 81$")
    print ("8 = Matcha covered cookie 85$")
def calcular_costo(p, cantidad):
    precios = [52, 67, 72, 66, 96, 77, 81, 85]
    costo = precios[p - 1] * cantidad
    return costo
def main():
    print("¿Qué deseas ordenar?")
    mostrar_menu()
    while True:
        try:
            p = int(input("Ingresa el numero de la galleta que deseas pedir (del 1 al 8): "))
            can = float(input("Ingresa la cantidad de galletas que quieres comprar: "))
            costot = calcular_costo(p, can)
            print(f"El costo sería de: ${costot:.2f}")

            otrao = input("¿Desea ordenar algo mas? (si/no): ")
            if otrao.lower() !="si":
                break
        except ValueError:
            print("Por favor, ingresa un numero valido.")

if __name__ == "__main__":
    main()

