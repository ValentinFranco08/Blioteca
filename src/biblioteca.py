class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, query):
        return [libro for libro in self.libros if query.lower() in libro.titulo.lower() or query.lower() in libro.autor.lower()]

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def listar_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]
