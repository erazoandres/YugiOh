import pygame
import random
import os


# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0,255,255)

# Configuración de la ventana
pygame.init()
WIDTH, HEIGHT = 400, 600
fondo = pygame.image.load("wall2.png")
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Memoria")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(VERDE)
os.environ['SDL_VIDEO_CENTERED'] = '1'


#CLASE DE CARTA
class Carta:
    def __init__(self, imagen):
        self.imagen = imagen
        self.volteada = False
        self.id = -1

    def voltear(self):
        self.volteada = True

    def dibujar(self, pos):
        if self.volteada:
            screen.blit(self.imagen, pos)
        else:
            # Dibujar una superficie oscura sobre la carta
            superficie_oscura = pygame.Surface((100, 150))
            superficie_oscura.fill(NEGRO)
            superficie_oscura.set_alpha(128)  # Establecer transparencia

    def id_set(self,data):
        self.id = data

    def id_get(self):
        return self.id


# Cargar las imágenes de las cartas
silueta = pygame.image.load("carta.png"),

imagenes_cartas = {
    "dragon": pygame.image.load("dragon.png"),
    "slifer": pygame.image.load("slifer.png"),
    "maga": pygame.image.load("maga.png"),
}

#ASOCIAMOS LAS IMAGENES Y NOMBRE  CON EL OBJETO DE LA CLASE CARTA
cartas = []
count = 0

for img in imagenes_cartas:

    cartas.extend([Carta(imagenes_cartas[img])])
    cartas[count].id_set(img)
    count+=1

random.shuffle(cartas)  # Mezclar las cartas

def obtener_indice_carta_clic(mouse_pos):
    for i, carta in enumerate(cartas):
        fila, columna = divmod(i, 4)  # Cambia 4 por el número de columnas que desees
        x, y = columna * 100, fila * 150  # Espaciado entre cartas
        rect_carta = pygame.Rect(x, y, 100, 150)  # Rectángulo que representa la carta
       
        
        if rect_carta.collidepoint(mouse_pos):
            # print(cartas[0].id_get())
            # print(cartas[i].id_get())
            return i
    return None

ejecutando = True
cartas_seleccionadas = []

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if len(cartas_seleccionadas) < 2:
                indice = obtener_indice_carta_clic(evento.pos)
              
                if indice is not None and indice not in cartas_seleccionadas:
       
                    cartas_seleccionadas.append(indice)
                    cartas[indice].voltear()
                  

    # Actualizar la pantalla
  
    for i, carta in enumerate(cartas):
        fila, columna = divmod(i, 4)  # Ahora tenemos 8 columnas
        x, y = columna * 100, fila * 150  # Espaciado entre cartas
        carta.dibujar((x, y))
    pygame.display.flip()

    # Verificar si se seleccionaron dos cartas y si son iguales
    if len(cartas_seleccionadas) == 2:
        
        indice1, indice2 = cartas_seleccionadas

        if cartas[indice1].imagen == cartas[indice2].imagen:
            print("Las cartas son iguales")
            # Las cartas son iguales, eliminarlas
            cartas[indice1] = None
            cartas[indice2] = None
        cartas_seleccionadas = []

# Salir del juego
pygame.quit()