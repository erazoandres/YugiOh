import pygame
import subprocess

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BIenvenido")

fondo = pygame.image.load("wall.png")
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))

pygame.mixer.music.load("soundtrack2.mp3")

if not pygame.mixer.music.get_busy():
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (25, 0, 50)

# Función para mostrar el menú
def mostrar_menu():
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rect_x <= event.pos[0] <= 600 and rect_y <= event.pos[1] <= 300:
                    # Ejecutar el archivo index.py
                    pygame.mixer.music.stop()
                    pygame.quit()
                    subprocess.run(["python", "main.py"])
                    running=False
                  
               
                elif rect_x <= event.pos[0] <= 600 and rect_y + 130 <= event.pos[1] <= rect_y+230:
                    running=False
                    

        # Dibujar el fondo y los elementos del menú
        # screen.fill(BLANCO)

        # Coordenadas para centrar los rectángulos
        rect_x = WIDTH // 2 - 200
        rect_y = HEIGHT // 2 - 100

        # Dibujar los rectángulos centrados
        pygame.draw.rect(screen, VERDE, (rect_x, rect_y, 400, 100))
        pygame.draw.rect(screen, VERDE, (rect_x, rect_y + 130, 400, 100))

        # Dibujar texto en los botones del menú
        font = pygame.font.Font(None, 36)
        texto_iniciar = font.render("Iniciar Juego", True, BLANCO)
        texto_salir = font.render("Salir", True, BLANCO)
        screen.blit(texto_iniciar, (rect_x + 120, rect_y + 30))
        screen.blit(texto_salir, (rect_x + 160, rect_y + 160))

        # Actualizar la pantalla
        pygame.display.flip()

screen.blit(fondo, (0, 0))

# Llamar a la función para mostrar el menú
mostrar_menu()

# Salir del programa
pygame.quit()