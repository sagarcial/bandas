import tkinter as tk
from random import choice, randint
from banda import Banda
from musico import Musico
from instrumento import Instrumento

# Crear una ventana principal de Tkinter
ventana = tk.Tk()
ventana.title("Banda Los Rítmicos")

# Crear una instancia de la banda y músicos
instrumentos = [
    Instrumento("Piano", "piano.png"),  # Reemplaza "piano.png" con la ruta correcta a la imagen
    Instrumento("Guitarra", "guitarra.png"),
    # Agrega más instrumentos con sus imágenes aquí
]
b = Banda("Los Rítmicos", instrumentos)

# Función para crear músicos aleatorios y actualizar la GUI
def crear_musicos_y_actualizar():
    b.crear()
    actualizar_info_banda()

# Función para afinar instrumentos y actualizar la GUI
def afinar_instrumentos_y_actualizar():
    b.afinar_instrumentos()
    actualizar_info_banda()

# Función para actualizar la información de la banda en la GUI
def actualizar_info_banda():
    # Borrar cualquier información anterior
    for widget in ventana.winfo_children():
        widget.destroy()

    # Mostrar el nombre de la banda
    label_banda = tk.Label(ventana, text="Nombre de la banda: " + b.nombre)
    label_banda.pack()

    # Mostrar imágenes de los músicos
    for musico in b.integrantes:
        imagen_musico = tk.PhotoImage(file=musico.imagen)
        label_musico = tk.Label(ventana, image=imagen_musico)
        label_musico.image = imagen_musico
        label_musico.pack()

# Botones para crear músicos y afinar instrumentos
boton_crear_musicos = tk.Button(ventana, text="Crear Músicos Aleatorios", command=crear_musicos_y_actualizar)
boton_crear_musicos.pack()

boton_afinar_instrumentos = tk.Button(ventana, text="Afinar Instrumentos", command=afinar_instrumentos_y_actualizar)
boton_afinar_instrumentos.pack()

# Inicializar la GUI con la información inicial de la banda
actualizar_info_banda()

ventana.mainloop()
