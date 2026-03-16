# efectos.py
import pygame

# Intentamos inicializar el mezclador de sonido
try:
    pygame.mixer.init()
    mixer_disponible = True
except Exception as e:
    print(f"[Aviso] No se pudo inicializar pygame.mixer: {e}")
    mixer_disponible = False

def reproducir_sonido_correcto():
    if mixer_disponible:
        try:
            pygame.mixer.Sound("correcto.wav").play()
        except Exception as e:
            print(f"[Aviso] No se pudo reproducir el sonido correcto: {e}")
    else:
        print("[Info] Sonido correcto omitido (pygame no disponible).")

def reproducir_sonido_error():
    if mixer_disponible:
        try:
            pygame.mixer.Sound("error.wav").play()
        except Exception as e:
            print(f"[Aviso] No se pudo reproducir el sonido de error: {e}")
    else:
        print("[Info] Sonido de error omitido (pygame no disponible).")
