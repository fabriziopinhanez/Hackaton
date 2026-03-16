# interfaz.py
import tkinter as tk

def crear_ventana():
    """Crea la ventana principal del juego."""
    ventana = tk.Tk()
    ventana.title("Trivia Game")
    ventana.geometry("400x300")
    ventana.resizable(False, False)  # Evita que el usuario cambie el tamaño
    return ventana

def crear_etiqueta(ventana):
    """Crea la etiqueta donde se mostrará la pregunta."""
    etiqueta = tk.Label(
        ventana,
        text="",
        font=("Arial", 14),
        wraplength=350,   # Ajusta el texto si es muy largo
        justify="center"
    )
    etiqueta.pack(pady=20)
    return etiqueta

def crear_botones(ventana, cantidad=3):
    """Crea los botones para las opciones de respuesta."""
    botones = []
    for i in range(cantidad):
        b = tk.Button(
            ventana,
            text="",
            width=20,
            height=2,
            font=("Arial", 12),
            bg="#f0f0f0",   # Color de fondo inicial
            activebackground="#d0d0d0"  # Color al presionar
        )
        b.pack(pady=5)
        botones.append(b)
    return botones

