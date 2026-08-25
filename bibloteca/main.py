from modelos.libro import Libro
from servicios.prestamo import realizar_prestamo, realizar_devolucion, consultar_disponibilidad

print("--- SISTEMA DE BIBLIOTECA ---")

mi_libro = Libro("Trucos de Python", "Alguien que paso muchas hs", "9582-3247")

print(consultar_disponibilidad(mi_libro))
print(realizar_prestamo(mi_libro))
print(consultar_disponibilidad(mi_libro))
print(realizar_prestamo(mi_libro))
print(realizar_devolucion(mi_libro))
print(consultar_disponibilidad(mi_libro))