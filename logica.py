# logica.py
from tkinter import messagebox
from datos import cargar_preguntas
from efectos import reproducir_sonido_correcto, reproducir_sonido_error

preguntas = cargar_preguntas()
puntaje = 0
indice = 0

def verificar_respuesta(opcion, etiqueta, botones, ventana):
    global puntaje, indice
    correcta = preguntas[indice]["respuesta"]
    if opcion == correcta:
        puntaje += 1
        reproducir_sonido_correcto()
        messagebox.showinfo("Correcto", "¡Bien hecho!")
    else:
        reproducir_sonido_error()
        messagebox.showerror("Incorrecto", f"La respuesta correcta era: {correcta}")
    
    indice += 1
    if indice < len(preguntas):
        mostrar_pregunta(etiqueta, botones)
    else:
        messagebox.showinfo("Fin del juego", f"Tu puntaje final es: {puntaje}/{len(preguntas)}")
        ventana.quit()

def mostrar_pregunta(etiqueta, botones):
    pregunta = preguntas[indice]["pregunta"]
    opciones = preguntas[indice]["opciones"]
    etiqueta.config(text=pregunta)
    
    for i, opcion in enumerate(opciones):
        botones[i].config(text=opcion, command=lambda opt=opcion: verificar_respuesta(opt, etiqueta, botones, etiqueta.master))

