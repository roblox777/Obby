x =  int (input("escribe un numero entero menor a 2000: "))
while x < 2000:
    print ("este es tu numero", x , "y es menor a 2000 le voy a sumar uno hasta llegar a la meta")
    x += 1
if x == 2000:
    print ("felicidades no sabes seguir instrucciones :/")
else:
    print("No se hizo nada ya que escribiste un numero mayor, ya pon mas atencion")