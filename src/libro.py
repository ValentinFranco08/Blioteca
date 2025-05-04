class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) - {estado}"


class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, tamano_mb):
        super().__init__(titulo, autor, isbn)
        self.tamano_mb = tamano_mb

    def descargar(self):
        return f"✅ El libro digital '{self.titulo}' está siendo descargado. Tamaño: {self.tamano_mb} MB."
