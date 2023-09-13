import tkinter as tk
from PIL import Image, ImageTk  # Importa PIL (Pillow) para trabajar con imágenes
from banda import Banda
from instrumento import Piano, Guitarra, Saxofon, Bajo, Flauta

# Crear una instancia de la banda y músicos
mi_banda = Banda("Los Rítmicos", [Piano(), Guitarra(), Saxofon(), Bajo(), Flauta()])
mi_banda.crear()

# Crear una función para cargar imágenes de los instrumentos
def cargar_imagenes():
    imagenes = {}
    for musico in mi_banda.integrantes:
        instrumento_nombre = musico.instrumento_toca.nombre.lower()
        imagen_path = f"{instrumento_nombre}.png"  # Asegúrate de que tienes las imágenes en la misma carpeta
        imagen = Image.open(imagen_path)  # Abre la imagen con PIL
        imagen_tk = ImageTk.PhotoImage(imagen)  # Convierte la imagen a un formato que tkinter pueda mostrar
        imagenes[instrumento_nombre] = imagen_tk
    return imagenes

# Función para afinar los instrumentos y mostrar información en la interfaz
def afinar_instrumentos_y_mostrar_info():
    afinar_text.delete(1.0, tk.END)  # Limpiar el área de texto de afinado
    afinar_text.insert(tk.END, "Afinando...\n")  # Mostrar "Afinando..." en el área de texto
    imagenes = cargar_imagenes()  # Cargar imágenes de los instrumentos
    for musico in mi_banda.integrantes:
        instrumento_nombre = musico.instrumento_toca.nombre.lower()
        afinar_text.insert(tk.END, f"Afinando {musico.instrumento_toca.nombre}...\n")
        afinar_text.image_create(tk.END, image=imagenes[instrumento_nombre])  # Mostrar la imagen
        musico.afinar_instrumento()
    mostrar_informacion()

# Función para mostrar la información de la banda en la interfaz
def mostrar_informacion():
    info_text.delete(1.0, tk.END)  # Limpiar el área de texto de información
    info_text.insert(tk.END, "Nombre de la banda: " + mi_banda.nombre + "\n")
    
    info_text.insert(tk.END, "Instrumentos en la banda:\n")
    for instrumento in mi_banda.instrumentos:
        info_text.insert(tk.END, "- " + instrumento.nombre + "\n")
    
    info_text.insert(tk.END, "Integrantes de la banda:\n")
    for musico in mi_banda.integrantes:
        info_text.insert(tk.END, "- Nombre: " + musico.nombre + ", Instrumento: " + musico.instrumento_toca.nombre + "\n")

# Crear la ventana de tkinter
root = tk.Tk()
root.title("Banda Musical")

# Crear botones y elementos de interfaz
afinar_button = tk.Button(root, text="Afinar Instrumentos", command=afinar_instrumentos_y_mostrar_info)
info_text = tk.Text(root, width=40, height=10)
afinar_text = tk.Text(root, width=40, height=4)

# Colocar los elementos en la ventana
afinar_button.pack()
afinar_text.pack()
info_text.pack()

# Mostrar información inicial al iniciar la aplicación
mostrar_informacion()

# Iniciar la aplicación de tkinter
root.mainloop()
