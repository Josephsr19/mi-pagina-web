# adivinar.py

import random

def main():
    print("Juego: Adivina el número (entre 1 y 100)")
    secreto = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            intento = int(input("Tu intento: "))
        except ValueError:
            print("Introduce un número válido.")
            continue
        intentos += 1
        if intento == secreto:
            print(f"¡Correcto! Adivinaste en {intentos} intento(s).")
            break
        elif intento < secreto:
            print("El número secreto es MAYOR.")
        else:
            print("El número secreto es MENOR.")

if __name__ == "__main__":
    main()
