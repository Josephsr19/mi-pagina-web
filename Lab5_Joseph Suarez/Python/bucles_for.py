# bucles_for.py

def main():
    numeros = [1, 2, 3, 4, 5]
    print("Lista:", numeros)
    print("Cuadrados:")
    for x in numeros:
        print(f"{x}^2 = {x**2}")

    # ejemplo con entrada del usuario
    entrada = input("Introduce números separados por comas (ej: 2,3,4) o ENTER para salir: ")
    if entrada.strip():
        try:
            lista = [int(i.strip()) for i in entrada.split(",")]
            for v in lista:
                print(f"{v}^2 = {v**2}")
        except ValueError:
            print("Formato incorrecto. Asegúrate de usar sólo números enteros separados por comas.")

if __name__ == "__main__":
    main()
