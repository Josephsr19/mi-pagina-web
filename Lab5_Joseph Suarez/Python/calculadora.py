# calculadora.py

def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b):
    if b == 0:
        return None
    return a / b

def main():
    print("Calculadora básica")
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Entrada inválida. Usa números.")
        return

    print("Operaciones:")
    print(f"{a} + {b} = {suma(a,b)}")
    print(f"{a} - {b} = {resta(a,b)}")
    print(f"{a} * {b} = {multiplicacion(a,b)}")
    div = division(a,b)
    if div is None:
        print("División entre 0: operación no permitida.")
    else:
        print(f"{a} / {b} = {div}")

if __name__ == "__main__":
    main()
