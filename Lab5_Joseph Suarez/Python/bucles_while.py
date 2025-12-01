# bucles_while.py

def main():
    print("Introduce números. Para terminar, escribe 0.")
    while True:
        try:
            n = int(input("Número: "))
        except ValueError:
            print("Entrada no válida. Intenta de nuevo.")
            continue
        if n == 0:
            print("Fin del bucle.")
            break
        print(f"Has introducido {n}.")

if __name__ == "__main__":
    main()
