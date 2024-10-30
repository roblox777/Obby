print("Bienvenido al restaurante 'Mao Ze Tsung'")
ct = 0
ta = 0

while True:
    print("Menu:")
    print(" 1. Rollos primavera ---- $23 la pieza")
    print(" 2. Dumplings ----- $27 la pieza")
    print(" 3. Arroz frito ---- $54")
    print(" 4. Sopa Zhen Jing ---- $64")
    print(" 5. Sopa Wantan ---- $67")
    print(" 6. Sopa Hanchow ---- $72")
    print(" 7. Chaufan ---- $39")
    print(" 8. Pollo agridulce ---- $58")
    
    op = int(input("Inserta el número de la comida que deseas: "))
    
    if op == 1:
        print("Has seleccionado los rollos primavera.")
        c = float(input("¿Qué cantidad deseas?: "))
        c1 = 23 * c
    elif op == 2:
        print("Has seleccionado los dumplings.")
        c = float(input("¿Qué cantidad deseas?: "))
        c1 = 27 * c
    elif op == 3:
        print("Has seleccionado el arroz frito.")
        c = float(input("¿Qué cantidad deseas?: "))
        c1 = 54 * c
    elif op == 4:
        print("Has seleccionado la sopa Zhen Jing.")
        c = float(input("¿Qué cantidad deseas?: "))
        c1 = 64 * c
    elif op == 5:
        print("Has seleccionado la sopa Wantan.")
        c = float(input("¿Qué cantidad deseas?: "))
        c1 = 67 * c
    elif op == 6:
        print("Has seleccionado la sopa Hanchow.")
        c = float(input("¿Qué cantidad deseas?: "))
        c1 = 72 * c
    elif op == 7:
        print("Has seleccionado el Chaufan.")
        c = float(input("¿Qué cantidad deseas?: "))
        c1 = 39 * c
    elif op == 8:
        print("Has seleccionado el pollo agridulce.")
        c = float(input("¿Qué cantidad deseas?: "))
        c1 = 58 * c
    else:
        print("La opción que has elegido no existe :(")
        continue

    ct += c1
    ta += c  # Acumula el total de artículos
    print("El costo sería de: ", ct)
    
    otr = input("¿Deseas comprar algo más? (si/no): ")
    if otr.lower() != "si":
        break

# Aplicar descuentos
if ta > 15:
    ct -= 77
    print("Se ha aplicado un descuento de $77 al haber comprado más de 15 artículos :)")

if ct > 1000:
    ct -= 100
    print("Se han descontado $100 por su compra superior a $1000.")
elif ct > 500:
    ct -= 60
    print("Se ha descontado el costo de envío de $60 por su compra superior a $500.")

print("¡Gracias por su compra! :)")
print("El total de su compra es:", ct)