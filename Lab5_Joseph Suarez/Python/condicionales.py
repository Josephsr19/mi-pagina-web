# condicionales.py

def main():
    try:
        n = int(input("Introduce un número entero: "))
    except ValueError:
        print("Entrada no válida. Debes introducir un número entero.")
        return

    if n % 2 == 0:
        print(f"{n} es PAR.")
    else:
        print(f"{n} es IMPAR.")

if __name__ == "__main__":
    main()
