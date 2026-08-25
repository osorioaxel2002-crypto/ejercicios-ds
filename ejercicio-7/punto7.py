def analizar_temperaturas(registros):
    temp_max = max(registros)
    temp_min = min(registros)

    prom = sum(registros) / len(registros)
    
    return temp_max, temp_min, prom

temperaturas_prueba = [25.5, 28.0, 21.5, 30.0, 19.0, 24.5, 26.0]

print("Analizando los registros...")

maxima, minima, prom = analizar_temperaturas(temperaturas_prueba)


print("\n---TEMPERATURAS---")
print(f"Temperatura máxima: {maxima}°C")
print(f"Temperatura mínima: {minima}°C")
print(f"Temperatura promedio: {prom:.2f}°C")