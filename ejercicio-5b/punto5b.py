
CONTRASEÑA_CORRECTA = "Admin1234"

contador = 0
while contador < 3:
    ingreso = input("Ingrese su contraseña: ")
    
    if ingreso == CONTRASEÑA_CORRECTA:
        print("\n¡Inicio de sesión exitoso! Bienvenido.")
        break 
        
    else:
        intentos = intentos + 1
        intentos_restantes = 3 - contador
       
        if intentos < 3:
            print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos.\n")
        else:
            print("\n¡Cuenta bloqueada! Agotaste tus 3 intentos.")