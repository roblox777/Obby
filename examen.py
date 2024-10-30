print ("Calculadora de Indice de masa corporal ")
p = float(input("Por favor ingresa tu peso: "))
a = float(input("Por favor ingresa tu altura (en metros): "))
c = p /a**2
print ("Tu indice de masa corporal es: " , c)
if c <18.5:
    print ("Tu peso es bajo")
elif 18.5 <= c < 25:
    print ("tu peso es normal")
elif 25 <= c < 30:
    print ("tienes sobrepeso.")
else:
    print ("tienes obesidad.")