def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False):
    if precio_base <= 0 or porcentaje_descuento < 0:
        raise ValueError("El precio base debe ser mayor a 0 y el descuento no puede ser negativo.")
    
    descuento_plata = precio_base * (porcentaje_descuento / 100)
    precio_rebajado = precio_base - descuento_plata
    
    if es_vip == True:
        descuento_vip = precio_rebajado * 0.05
        precio_rebajado = precio_rebajado - descuento_vip
        
    return precio_rebajado

print("--- Pruebas De La Funcion ---")

resultado1 = calcular_precio_final(1000)
print(f"Prueba 1 (Solo precio base $1000): ${resultado1}")

resultado2 = calcular_precio_final(1000, 20)
print(f"Prueba 2 (Precio $1000, 20% desc): ${resultado2}")

resultado3 = calcular_precio_final(1000, 20, True)
print(f"Prueba 3 (Precio $1000, 20% desc, es VIP): ${resultado3}")

print("Prueba 4 (Provocando un error a propósito con precio negativo):")
try:
    calcular_precio_final(-500)
except ValueError as error_capturado:
    print(f"El programa atajó el error Mensaje: {error_capturado}")