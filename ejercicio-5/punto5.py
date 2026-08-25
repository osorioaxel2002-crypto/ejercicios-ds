
contrasena = input("Ingrese una nueva contraseña: ")

tiene_mayus = False
tiene_minus = False

for letra in contrasena:
    if letra.isupper():
        tiene_mayus = True  
    
    if letra.islower():
        tiene_minus = True 

longitud_correcta = len(contrasena) >= 8

if longitud_correcta and tiene_mayus and tiene_minus:
    print("\n¡Excelente! La contraseña es segura y válida.")
else:
    print("\nError: La contraseña debe tener al menos 8 caracteres, una mayúscula y una minúscula.")