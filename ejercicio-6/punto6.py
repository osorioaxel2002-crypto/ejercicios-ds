while True:
    print("\n" + "-"*30)
    print("      MENÚ INTERACTIVO      ")
    print("-"*30)
    print("A. Sumar los primeros N números naturales")
    print("B. Encontrar números divisibles por 3 en un rango")
    print("C. Salir")
    
    opcion = input("\nElegí una opción (A, B o C): ").upper()
    
    match opcion:
        case "A":
            print("\n--- Suma de N números ---")
            n = int(input("Ingresá el número N: "))
            
            suma = 0
           
            for i in range(1, n + 1):
                suma = suma + i
                
            print(f"Resultado: La suma de los primeros {n} números es {suma}")
            
        case "B":
            print("\n--- Divisibles por 3 ---")
            inicio = int(input("Ingresá el número inicial del rango: "))
            fin = int(input("Ingresá el número final del rango: "))
            
            print(f"Los números divisibles por 3 entre {inicio} y {fin} son:")
            
            for numero in range(inicio, fin + 1):
                if numero % 3 == 0:
                    print(f"- {numero}")
                    
        case "C":
            print("\n¡Saliendo del programa")
            break
            
        case _:
            print("\nOpción incorrecta. Por favor                                                                  , ingresá A, B o C.")