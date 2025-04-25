import tkinter as tk
from tkinter import messagebox

# === Clases del sistema ===

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({'Disponible' if self.disponible else 'Prestado'})"


class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, tamano):
        super().__init__(titulo, autor, isbn)
        self.tamano = tamano  # en MB

    def __str__(self):
        return f"{self.titulo} (Digital, {self.tamano} MB) - {self.autor} ({'Disponible' if self.disponible else 'Prestado'})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def pedir_prestado(self, libro):
        if len(self.libros_prestados) >= 3:
            return f"⚠️ {self.nombre} ya tiene 3 libros prestados."
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            return f"✅ {self.nombre} ha prestado '{libro.titulo}'."
        return f"⚠️ '{libro.titulo}' no está disponible."

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            return f"✅ {self.nombre} devolvió '{libro.titulo}'."
        return f"⚠️ {self.nombre} no tiene prestado '{libro.titulo}'."


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, id_usuario):
        return next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

    def listar_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

    def buscar_libro_por_titulo(self, titulo):
        return next((l for l in self.libros if l.titulo.lower() == titulo.lower()), None)


# === Interfaz Tkinter ===

class InterfazBiblioteca:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.root = root
        self.root.title("📚 Gestión de Biblioteca")

        # Widgets
        self.label_info = tk.Label(root, text="Sistema de Gestión de Biblioteca", font=("Arial", 14))
        self.label_info.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.boton_agregar = tk.Button(self.frame, text="Agregar Libro", width=15, command=self.agregar_libro)
        self.boton_agregar.grid(row=0, column=0, padx=5)

        self.boton_usuario = tk.Button(self.frame, text="Registrar Usuario", width=15, command=self.registrar_usuario)
        self.boton_usuario.grid(row=0, column=1, padx=5)

        self.boton_prestar = tk.Button(self.frame, text="Prestar Libro", width=15, command=self.prestar_libro)
        self.boton_prestar.grid(row=1, column=0, padx=5, pady=5)

        self.boton_devolver = tk.Button(self.frame, text="Devolver Libro", width=15, command=self.devolver_libro)
        self.boton_devolver.grid(row=1, column=1, padx=5, pady=5)

        self.boton_disponibles = tk.Button(root, text="📘 Ver Libros Disponibles", command=self.mostrar_libros)
        self.boton_disponibles.pack(pady=5)

        self.boton_usuarios = tk.Button(root, text="👥 Ver Usuarios Registrados", command=self.mostrar_usuarios)
        self.boton_usuarios.pack(pady=5)

    def agregar_libro(self):
        def guardar():
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            isbn = entry_isbn.get()
            es_digital = var_digital.get()
            if es_digital:
                try:
                    tamano = float(entry_tamano.get())
                    libro = LibroDigital(titulo, autor, isbn, tamano)
                except ValueError:
                    messagebox.showerror("Error", "Tamaño inválido.")
                    return
            else:
                libro = Libro(titulo, autor, isbn)
            self.biblioteca.agregar_libro(libro)
            messagebox.showinfo("Éxito", f"Libro '{titulo}' agregado.")
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Agregar Libro")

        tk.Label(top, text="Título:").grid(row=0, column=0)
        tk.Label(top, text="Autor:").grid(row=1, column=0)
        tk.Label(top, text="ISBN:").grid(row=2, column=0)

        entry_titulo = tk.Entry(top)
        entry_autor = tk.Entry(top)
        entry_isbn = tk.Entry(top)
        entry_titulo.grid(row=0, column=1)
        entry_autor.grid(row=1, column=1)
        entry_isbn.grid(row=2, column=1)

        var_digital = tk.BooleanVar()
        chk_digital = tk.Checkbutton(top, text="¿Es digital?", variable=var_digital)
        chk_digital.grid(row=3, column=0, columnspan=2)

        tk.Label(top, text="Tamaño (MB):").grid(row=4, column=0)
        entry_tamano = tk.Entry(top)
        entry_tamano.grid(row=4, column=1)

        btn_guardar = tk.Button(top, text="Guardar", command=guardar)
        btn_guardar.grid(row=5, column=0, columnspan=2, pady=5)

    def registrar_usuario(self):
        def guardar_usuario():
            nombre = entry_nombre.get()
            id_usuario = entry_id.get()
            if self.biblioteca.buscar_usuario(id_usuario):
                messagebox.showerror("Error", "ID ya registrado.")
                return
            self.biblioteca.registrar_usuario(Usuario(nombre, id_usuario))
            messagebox.showinfo("Éxito", f"Usuario '{nombre}' registrado.")
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Registrar Usuario")

        tk.Label(top, text="Nombre:").grid(row=0, column=0)
        tk.Label(top, text="ID Usuario:").grid(row=1, column=0)

        entry_nombre = tk.Entry(top)
        entry_id = tk.Entry(top)
        entry_nombre.grid(row=0, column=1)
        entry_id.grid(row=1, column=1)

        btn_guardar = tk.Button(top, text="Registrar", command=guardar_usuario)
        btn_guardar.grid(row=2, column=0, columnspan=2, pady=5)

    def prestar_libro(self):
        def prestar():
            usuario = self.biblioteca.buscar_usuario(entry_id.get())
            if not usuario:
                messagebox.showerror("Error", "Usuario no encontrado.")
                return
            libro = self.biblioteca.buscar_libro_por_titulo(entry_titulo.get())
            if not libro:
                messagebox.showerror("Error", "Libro no encontrado.")
                return
            resultado = usuario.pedir_prestado(libro)
            messagebox.showinfo("Resultado", resultado)
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Prestar Libro")

        tk.Label(top, text="ID Usuario:").grid(row=0, column=0)
        tk.Label(top, text="Título del Libro:").grid(row=1, column=0)

        entry_id = tk.Entry(top)
        entry_titulo = tk.Entry(top)
        entry_id.grid(row=0, column=1)
        entry_titulo.grid(row=1, column=1)

        btn_prestar = tk.Button(top, text="Prestar", command=prestar)
        btn_prestar.grid(row=2, column=0, columnspan=2, pady=5)

    def devolver_libro(self):
        def devolver():
            usuario = self.biblioteca.buscar_usuario(entry_id.get())
            if not usuario:
                messagebox.showerror("Error", "Usuario no encontrado.")
                return
            libro = self.biblioteca.buscar_libro_por_titulo(entry_titulo.get())
            if not libro:
                messagebox.showerror("Error", "Libro no encontrado.")
                return
            resultado = usuario.devolver_libro(libro)
            messagebox.showinfo("Resultado", resultado)
            top.destroy()

        top = tk.Toplevel(self.root)
        top.title("Devolver Libro")

        tk.Label(top, text="ID Usuario:").grid(row=0, column=0)
        tk.Label(top, text="Título del Libro:").grid(row=1, column=0)

        entry_id = tk.Entry(top)
        entry_titulo = tk.Entry(top)
        entry_id.grid(row=0, column=1)
        entry_titulo.grid(row=1, column=1)

        btn_devolver = tk.Button(top, text="Devolver", command=devolver)
        btn_devolver.grid(row=2, column=0, columnspan=2, pady=5)

    def mostrar_libros(self):
        disponibles = self.biblioteca.listar_libros_disponibles()
        libros_texto = "\n".join(str(libro) for libro in disponibles) or "No hay libros disponibles."
        messagebox.showinfo("Libros Disponibles", libros_texto)

    def mostrar_usuarios(self):
        if not self.biblioteca.usuarios:
            messagebox.showinfo("Usuarios", "No hay usuarios registrados.")
            return
        texto = ""
        for u in self.biblioteca.usuarios:
            prestados = ", ".join(libro.titulo for libro in u.libros_prestados) or "Ninguno"
            texto += f"{u.nombre} (ID: {u.id_usuario})\n  Prestados: {prestados}\n\n"
        messagebox.showinfo("Usuarios Registrados", texto)

# === Ejecutar la aplicación ===

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazBiblioteca(root)
    root.mainloop()
