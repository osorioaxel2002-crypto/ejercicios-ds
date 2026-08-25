class CuentaBancaria:
    def __init__(obj, titular, saldo=0.0):
        obj.titular = titular
        obj.saldo = saldo
    def depositar(obj, monto):
        if monto > 0:
            obj.saldo = obj.saldo + monto
            print(f"Depósito de ${monto} exitoso")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def retirar(obj, monto):
        if monto <= obj.saldo:
            obj.saldo = obj.saldo - monto
            print(f"Retiro de ${monto} exitoso")
        else:
            print(f"Fondos insuficientes")

    def mostrar_info(obj):
        print(f"-> Cuenta de {obj.titular} | Saldo actual: ${obj.saldo}")

print("--- Cuentas ---")

cuenta_axel = CuentaBancaria("Axel")
cuenta_axel.mostrar_info()


cuenta_uziel = CuentaBancaria("Osorio Uziel", 50000.0)
cuenta_uziel.mostrar_info()


print("\n--- Moviendo El Dinero De Axel ---")
cuenta_axel.depositar(15000)
cuenta_axel.mostrar_info()

cuenta_axel.retirar(3000)
cuenta_axel.mostrar_info()

print("\nCompra muy cara")
cuenta_axel.retirar(50000) 
cuenta_axel.mostrar_info()