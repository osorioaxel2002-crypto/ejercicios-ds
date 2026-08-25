def convertir_a_fahrenheit(celsius)  :
    resultado =  (celsius * 9/5)+ 32
    return resultado

def convertir_a_celsius(fahrenheit):
    resultado = (fahrenheit - 32) * 5/9
    return resultado
 
temperatura= float(input("Ingrese la temperatura "))
escala = input("Ingrese la escala original (C para Celsius, F para Fahrenheit): ")

if escala.upper() == "C": 
    resultado = convertir_a_fahrenheit(temperatura)
    escala = "Fahrenheit"
    print(f"El valor convertido es: {resultado} grados Fahrenheit")

elif escala.upper() == "F":
    resultado = convertir_a_celsius(temperatura)
    escala = "Celsius"
    print(f"El valor convertido es: {resultado} grados Celsius")
    
else:
    print("Escala incorrecta")
   