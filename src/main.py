from libro import Libro, LibroDigital
from usuario import Usuario
from biblioteca import Biblioteca

def mostrar_libros_disponibles(biblioteca):
    disponibles = biblioteca.listar_libros_disponibles()
    if disponibles:
        print("📘 Libros disponibles:")
        for libro in disponibles:
            print(libro)
    else:
        print("⚠️ No hay libros disponibles.")

def mostrar_usuarios(biblioteca):
    if biblioteca.usuarios:
        print("👥 Usuarios registrados:")
        for usuario in biblioteca.usuarios:
            libros = ", ".join([libro.titulo for libro in usuario.libros_prestados]) if usuario.libros_prestados else "Ninguno"
            print(f"{usuario.nombre} (ID: {usuario.id_usuario}) - Libros prestados: {libros}")
    else:
        print("⚠️ No hay usuarios registrados.")

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n📝 Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Registrar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Buscar libro")
        print("6. Listar libros disponibles")
        print("7. Listar usuarios registrados")
        print("8. Salir")

        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("ISBN del libro: ")
            libro_tipo = input("¿Es un libro digital? (s/n): ").lower()

            if libro_tipo == "s":
                tamano = float(input("Tamaño en MB: "))
                libro = LibroDigital(titulo, autor, isbn, tamano)
            else:
                libro = Libro(titulo, autor, isbn)
            
            biblioteca.agregar_libro(libro)
            print(f"✅ Libro '{titulo}' agregado correctamente.")

        elif opcion == "2":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            if biblioteca.buscar_usuario(id_usuario):
                print("⚠️ El ID ya está registrado. Intenta con otro.")
            else:
                usuario = Usuario(nombre, id_usuario)
                biblioteca.registrar_usuario(usuario)
                print(f"✅ Usuario '{nombre}' registrado correctamente.")

        elif opcion == "3":
            id_usuario = input("ID del usuario: ")
            usuario = biblioteca.buscar_usuario(id_usuario)
            if not usuario:
                print("⚠️ Usuario no registrado.")
                continue

            titulo_libro = input("Título del libro a prestar: ")
            libro = next((l for l in biblioteca.libros if l.titulo.lower() == titulo_libro.lower()), None)

            if libro:
                print(usuario.pedir_prestado(libro))
            else:
                print(f"⚠️ No se encontró el libro '{titulo_libro}'.")

        elif opcion == "4":
            id_usuario = input("ID del usuario: ")
            usuario = biblioteca.buscar_usuario(id_usuario)
            if not usuario:
                print("⚠️ Usuario no registrado.")
                continue

            titulo_libro = input("Título del libro a devolver: ")
            libro = next((l for l in usuario.libros_prestados if l.titulo.lower() == titulo_libro.lower()), None)

            if libro:
                print(usuario.devolver_libro(libro))
            else:
                print(f"⚠️ El usuario no tiene el libro '{titulo_libro}' prestado.")

        elif opcion == "5":
            query = input("Introduce el título o autor del libro a buscar: ")
            resultados = biblioteca.buscar_libro(query)
            if resultados:
                print("🔍 Resultados de la búsqueda:")
                for libro in resultados:
                    print(libro)
            else:
                print("⚠️ No se encontraron libros que coincidan con la búsqueda.")

        elif opcion == "6":
            mostrar_libros_disponibles(biblioteca)

        elif opcion == "7":
            mostrar_usuarios(biblioteca)

        elif opcion == "8":
            print("👋 Hasta luego!")
            break

        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
