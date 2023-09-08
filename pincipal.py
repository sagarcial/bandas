import tkinter as tk

# ... Tu código para crear la banda y los músicos ...

# Crear una ventana principal de Tkinter
ventana = tk.Tk()
ventana.title("Banda Los Rítmicos")

# Función para afinar los instrumentos
def afinar_instrumentos():
    b.afinar_instrumentos()
    b.consultar()

# Botón para afinar los instrumentos
boton_afinar = tk.Button(ventana, text="Afinar Instrumentos", command=afinar_instrumentos)
boton_afinar.pack()

# Cargar imágenes de los instrumentos
imagenes_instrumentos = []
for musico in b.integrantes:
    nombre_imagen = f"{musico.nombre}.png"  # Asegúrate de que los nombres de las imágenes coincidan con los nombres de los músicos
    imagen = tk.PhotoImage(file=nombre_imagen)
    imagenes_instrumentos.append(imagen)

# Crear etiquetas para mostrar las imágenes
for i, imagen in enumerate(imagenes_instrumentos):
    etiqueta_imagen = tk.Label(ventana, image=imagen)
    etiqueta_imagen.pack()

ventana.mainloop()
