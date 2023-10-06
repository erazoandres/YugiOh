import pygame
import subprocess

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 76)
pygame.display.set_caption("GANASTE")
BLANCO = (255, 255, 255)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    screen.fill((0, 0, 0))  # Limpiar la pantalla con color negro

    texto_victoria = font.render("¡Has ganado!", True, BLANCO)
    text_rect = texto_victoria.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(texto_victoria, text_rect)

    pygame.display.flip()

pygame.quit()