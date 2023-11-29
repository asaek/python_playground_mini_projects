import pygame.mixer

def print_hi():
    # Inicializar pygame
    pygame.mixer.init()

    # Cargar un archivo de audio
    sonido = pygame.mixer.Sound("02 - Kyary Pamyu Pamyu - No No No.flac")

    # Reproducir el sonido
    sonido.play()

    # Esperar a que termine la reproducción (opcional)
    duracion_ms = int(sonido.get_length() * 1000)
    pygame.time.delay(duracion_ms)


if __name__ == '__main__':
    print_hi()

