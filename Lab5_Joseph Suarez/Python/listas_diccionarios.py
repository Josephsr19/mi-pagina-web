# listas_diccionarios.py

def main():
    estudiantes = ["Juan", "Ana", "Luis"]
    print("Estudiantes iniciales:", estudiantes)

    # Mostrar cada estudiante
    for e in estudiantes:
        print(" -", e)

    # Añadir un estudiante
    nuevo = input("Añade un nuevo estudiante (o ENTER para omitir): ")
    if nuevo.strip():
        estudiantes.append(nuevo.strip())
        print("Lista actualizada:", estudiantes)

    # Diccionario de contacto
    contacto = {"nombre": "María", "correo": "maria@example.com"}
    print("Contacto:", contacto)
    print("Claves:", list(contacto.keys()))
    print("Valores:", list(contacto.values()))

    # Actualizar correo
    correo = input("Escribe un nuevo correo para María (o ENTER para dejar): ")
    if correo.strip():
        contacto["correo"] = correo.strip()
        print("Contacto actualizado:", contacto)

if __name__ == "__main__":
    main()
