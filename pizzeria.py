pequeña = {"Muzzarella":1800, "Napolitana":2200, "Jamon y Morrones":2500, "De La Casa":3000}
grande = {"Muzzarella":2300, "Napolitana":2700, "Jamon y Morrones":3000, "De La Casa":3500}
compra = True
carrito = {}
direccion = None
nombre = input(str("Como te llamas? "))

print(f"***¡Bienvenido {nombre}!***")

while compra:
  print("")
  print("***PIZZERIA LOS SEÑORES DE LA MUZZA***")
  print("")
  print("1- Ver lista de pizzas pequeñas")
  print("2- Ver lista de pizzas grandes")
  print("3- Ver compras")
  if direccion:
    print("4- Cambiar dirección de entrega")
  else:
    print("4- Registrar dirección de entrega")
  print("5- Finalizar compra")
  print("")
  eleccion = input("Introducí la opción deseada: ")
  eleccion=int(eleccion)

  ##Opción 1: Pizzas pequeñas
  if eleccion==1:
    print("Lista de pizzas pequeñas:")
    for pizza, precio in pequeña.items():
      print(f"{pizza} ${precio}")
    pizza_elegida = input("Elige una pizza pequeña: ")
    if pizza_elegida in pequeña:
      if pizza_elegida in carrito:
          carrito[pizza_elegida] += pequeña[pizza_elegida]
      else:
          carrito[pizza_elegida] = pequeña[pizza_elegida]
    else:
      print("Pizza no válida.")
  ##Opción 2: Pizzas grandes
  elif eleccion==2:
    print("Lista de pizzas grandes:")
    for pizza, precio in grande.items():
      print(f"{pizza} ${precio}")
    pizza_elegida = input("Elige una pizza grande: ")
    if pizza_elegida in grande:
      if pizza_elegida in carrito:
        carrito[pizza_elegida] += grande[pizza_elegida]
      else:
        carrito[pizza_elegida] = grande[pizza_elegida]
    else:
      print("Pizza no válida.")
  ##Opción 3: Ver carrito
  elif eleccion==3:
    print("Carrito de compras:")
    for pizza, total in carrito.items():
      print(f"{pizza}: ${total}")
  ##Opcion 4: Dirección
  elif eleccion==4:
    if direccion:
      direccion = input("Cambiar la dirección de entrega: ")
    else:
      direccion = input("Ingresa la dirección de entrega: ")
  ##Opción 5: Finalizar lA compra
  elif eleccion==5:
    if direccion:
      compra=False
    else:
      print("Debes ingresar una dirección para finalizar")
      while not direccion:
        direccion = input("Ingresa la dirección de entrega: ")
  else:
    print("Opción no válida")
##Mensaje final
total_compra = sum(carrito.values())
if direccion:
  print(f"El total de tu compra es: ${total_compra}")
  print(f"Tu pedido será entregado en la siguiente dirección: {direccion}")
  print(f"¡Gracias por tu compra {nombre}!")
else:
  print("No has ingresado una dirrección para que podamos hacer la entrega")
