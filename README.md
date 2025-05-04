# 📚 Gestión de Biblioteca

Un proyecto simple para modelar el sistema de gestión de una biblioteca, aplicando conceptos fundamentales de **Programación Orientada a Objetos (POO)**.

---

## 🎯 Objetivo

Desarrollar una aplicación que permita gestionar libros y usuarios en una biblioteca, utilizando:

- Clases y objetos  
- Atributos y métodos  
- Herencia  
- Encapsulamiento  

---

## 🧱 Estructura del Sistema

### 🔹 Clases principales:

- **📘 Libro**  
  Atributos: `título`, `autor`, `ISBN`, `disponible (bool)`

- **👤 Usuario**  
  Atributos: `nombre`, `ID`, `libros_prestados` (máximo 3)

- **🏛️ Biblioteca**  
  Atributos: `lista de libros`, `usuarios registrados`

---

## ⚙️ Funcionalidades

### 👤 Un Usuario puede:
- Pedir prestado un libro  
  _(solo si está disponible y no superó el límite de 3 libros)_
- Devolver un libro  

### 🏛️ La Biblioteca puede:
- Registrar nuevos usuarios  
- Agregar libros a su inventario  
- Buscar libros por **título** o **autor**

---

## 🌟 Extra (opcional)

- Crear una clase `LibroDigital` que **herede de `Libro`**, y agregue:
  - Atributo: `tamaño (MB)`
  - Método: `descargar()`

- Manejo de errores:
  - “📕 Libro no disponible”
  - “🙅 Usuario no registrado”
  - Entre otros casos relevantes

---

## 📦 Entrega

El proyecto debe estar **versionado con Git** y correctamente documentado en este repositorio.

