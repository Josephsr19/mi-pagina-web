# variables.py

def main():
    entero = 5
    flotante = 3.2
    texto = "Laboratorio 5"

    suma = entero + int(flotante)  
    multiplicacion = entero * flotante

    print("Entero:", entero)
    print("Flotante:", flotante)
    print("Texto:", texto)
    print("Suma (entero + int(flotante)):", suma)
    print("Multiplicación (entero * flotante):", multiplicacion)

   
    a = int(input("Introduce un número entero: "))
    b = float(input("Introduce un número (puede tener decimales): "))
    print(f"La suma de {a} + {b} = {a + b}")

if __name__ == "__main__":
    main()
