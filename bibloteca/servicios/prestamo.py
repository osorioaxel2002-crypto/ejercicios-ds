from modelos.libro import Libro

def realizar_prestamo(libro):
    if libro.disponible == True:
        libro.disponible = False
        return f"Éxito! Se prestó el libro '{libro.titulo}'."
    else:
        return f"El libro '{libro.titulo}' ya está prestado."

def realizar_devolucion(libro):
    if libro.disponible == False:
        libro.disponible = True
        return f" Devolucion exitosa '{libro.titulo}'!"
    else:
        return f"El libro '{libro.titulo}' ya estaba en biblioteca."

def consultar_disponibilidad(libro):
    if libro.disponible == True:
        return f"El libro '{libro.titulo}' está disponible."
    else:
        return f"El libro '{libro.titulo}' no está disponible."