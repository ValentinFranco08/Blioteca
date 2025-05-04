class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

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
