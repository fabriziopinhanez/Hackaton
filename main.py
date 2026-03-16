# main.py
from interfaz import crear_ventana, crear_etiqueta, crear_botones
from logica import mostrar_pregunta

def main():
    # Crear la ventana principal
    ventana = crear_ventana()
    
    # Crear la etiqueta donde se mostrará la pregunta
    etiqueta = crear_etiqueta(ventana)
    
    # Crear los botones de opciones
    botones = crear_botones(ventana)
    
    # Mostrar la primera pregunta
    mostrar_pregunta(etiqueta, botones)
    
    # Mantener la ventana abierta
    ventana.mainloop()

if __name__ == "__main__":
    main()
