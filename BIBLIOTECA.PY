# Clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # El libro está disponible al principio

    def __str__(self):
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros que ha prestado

    def pedir_prestado(self, libro):
        if len(self.libros_prestados) >= 3:
            return f"⚠️ El usuario {self.nombre} ya tiene el máximo de 3 libros prestados."
        if not libro.disponible:
            return f"⚠️ El libro '{libro.titulo}' no está disponible."
        self.libros_prestados.append(libro)
        libro.disponible = False
        return f"✅ El libro '{libro.titulo}' ha sido prestado a {self.nombre}."

    def devolver_libro(self, libro):
        if libro not in self.libros_prestados:
            return f"⚠️ El usuario {self.nombre} no tiene el libro '{libro.titulo}' prestado."
        self.libros_prestados.remove(libro)
        libro.disponible = True
        return f"✅ El libro '{libro.titulo}' ha sido devuelto."

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, query):
        # Buscar por título o autor
        return [libro for libro in self.libros if query.lower() in libro.titulo.lower() or query.lower() in libro.autor.lower()]

    def buscar_usuario(self, id_usuario):
        # Buscar usuario por ID
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def listar_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

# Clase LibroDigital (hereda de Libro)
class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, tamano_mb):
        super().__init__(titulo, autor, isbn)
        self.tamano_mb = tamano_mb  # Tamaño en MB

    def descargar(self):
        return f"✅ El libro digital '{self.titulo}' está siendo descargado. Tamaño: {self.tamano_mb} MB."

# Funciones de utilidad
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

# Función principal para interactuar con el sistema
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
