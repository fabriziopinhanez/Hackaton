# TRIVIA-HACKATON
🎮 Trivia Game en Python
Un juego de trivia desarrollado en Python con Tkinter para la interfaz gráfica y pygame para los efectos de sonido.
Las preguntas se cargan desde un archivo externo en formato JSON, lo que facilita su edición y ampliación.

📂 Estructura del proyecto
Código
trivia/
│── datos.py          # Carga las preguntas desde Preguntas.json
│── efectos.py        # Maneja sonidos (pygame) con manejo de errores
│── interfaz.py       # Construye la ventana y botones con Tkinter
│── logica.py         # Lógica del juego: puntaje, validación, flujo
│── Preguntas.json    # Archivo externo con las preguntas
│── README.md         # Documentación del proyecto
│── main.py           # Punto de entrada para ejecutar el juego
⚙️ Requisitos
Python 3.8 a 3.12 (probado en 3.11.9)

Librerías:

tkinter (incluida en Python por defecto)

pygame

📥 Instalación
Clona o descarga este repositorio.

Abre la carpeta en Visual Studio Code.

Crea un entorno virtual:

bash
py -m venv venv
Activa el entorno virtual:

En Windows CMD/PowerShell:

bash
venv\Scripts\activate
En Git Bash:

bash
source venv/Scripts/activate
Instala las dependencias:

bash
py -m pip install pygame
▶️ Ejecución
En la terminal de Visual Studio Code, ejecuta:

bash
py main.py
Esto abrirá la ventana del juego.

🎨 Interfaz
Una ventana de 400x300 px.

Arriba: la pregunta en texto grande.

Debajo: tres botones con las opciones de respuesta.

Al hacer clic:

✅ Correcto → aparece un cuadro emergente con “¡Bien hecho!” y se reproduce el sonido correcto.

❌ Incorrecto → aparece un cuadro emergente con la respuesta correcta y se reproduce el sonido de error.

Al terminar todas las preguntas → aparece un cuadro con tu puntaje final.

📜 Preguntas (Preguntas.json)
Ejemplo de estructura:

json
[
  {
    "pregunta": "¿Cuál es la capital de Francia?",
    "opciones": ["París", "Roma", "Madrid"],
    "respuesta": "París"
  },
  {
    "pregunta": "¿Quién pintó la Mona Lisa?",
    "opciones": ["Picasso", "Leonardo da Vinci", "Van Gogh"],
    "respuesta": "Leonardo da Vinci"
  }
]
Puedes añadir tantas preguntas como quieras editando este archivo.

🛠️ Archivos principales
datos.py → Carga las preguntas desde Preguntas.json.

efectos.py → Reproduce sonidos de acierto/error con manejo de errores.

interfaz.py → Construye la ventana, etiqueta y botones con Tkinter.

logica.py → Controla el flujo del juego, puntaje y validación de respuestas.

main.py → Punto de entrada que une todo y ejecuta el juego.

👨‍💻 Autor
Proyecto desarrollado por Fabrizio como práctica de Python, Tkinter y pygame.

