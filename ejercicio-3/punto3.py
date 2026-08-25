pasaje=float(input("Ingrese precio de pasaje $"))
noches=int(input("Ingrese las noches del viaje: "))
alojamiento= float(input("Ingrese el precio de alojamiento por noche $ "))
dineroDisponible = float(input("Ingresá tu presupuesto disponible: $"))

#Calculo
total= pasaje +(alojamiento*noches)
alcanza = dineroDisponible >= total
print("\n--- RESUMEN DEL VIAJE ---")
print(f"Costo del pasaje: ${pasaje}")
print(f"Costo de alojamiento total: ${noches * alojamiento}")
print(f"Costo total del viaje: ${total}")
print(f"Dinero disponible: ${dineroDisponible}")
print(f"¿Alcanza el dinero?: {alcanza}")