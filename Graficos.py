# main.py
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import random
from instrumento import Instrumento
from musico import Músico

# Crear una lista de instrumentos
instrumentos = [Instrumento("Piano"), Instrumento("Guitarra"), Instrumento("Bajo"), Instrumento("Saxofón")]

# Función para mostrar una imagen aleatoria del instrumento
def mostrar_imagen_aleatoria():
    musico = Músico("Músico", random.choice(instrumentos))
    imagen_path = f"imagenes/{musico.instrumento.nombre}.png"
    imagen = Image.open(imagen_path)
    imagen = imagen.resize((200, 200), Image.ANTIALIAS)
    imagen = ImageTk.PhotoImage(imagen)

    imagen_label.config(image=imagen)
    imagen_label.image = imagen

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Músicos e Instrumentos")

# Botón para mostrar una imagen aleatoria
boton_mostrar = Button(ventana, text="Mostrar Instrumento Aleatorio", command=mostrar_imagen_aleatoria)
boton_mostrar.pack(pady=10)

# Label para mostrar la imagen
imagen_label = Label(ventana)
imagen_label.pack()

ventana.mainloop()
