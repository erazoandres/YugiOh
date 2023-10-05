#LIBRERIAS
import pygame
import random
import os
import copy

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 255)

# Configuración de la ventana
pygame.init()
WIDTH, HEIGHT = 400, 600
fondo = pygame.image.load("wall2.png")
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Memoria")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(VERDE)
os.environ['SDL_VIDEO_CENTERED'] = '1'

# CLASE DE CARTA
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
            screen.blit(silueta, pos)

    def id_set(self, data):
        self.id = data

    def id_get(self):
        return self.id


# Cargar las imágenes de las cartas
silueta = pygame.image.load("carta.png")

imagenes_cartas = {
    "dragon": pygame.image.load("dragon.png"),
    "slifer": pygame.image.load("slifer.png"),
    "maga": pygame.image.load("maga.png"),
}

# ASOCIAMOS LAS IMAGENES Y NOMBRE CON EL OBJETO DE LA CLASE CARTA
cartas = []
count = 0

for img in imagenes_cartas:
    cartas.extend([Carta(imagenes_cartas[img])])
    cartas[count].id_set(img)
    count += 1

# RELLENAMOS CON MAS CARTAS
for i in range(len(cartas)):
    for j in range(3):
        cartas.append(copy.copy(cartas[i]))

# Mezclar la lista con las cartas
random.shuffle(cartas)  


#OBTENER DATOS DEL OBJETO CLICKEADO
def obtener_indice_carta_clic(mouse_pos):
    for i, carta in enumerate(cartas):
        fila, columna = divmod(i, 4)  # Cambia 4 por el número de columnas que desees
        x, y = columna * 100, fila * 150  # Espaciado entre cartas
        rect_carta = pygame.Rect(x, y, 100, 150)  # Rectángulo que representa la carta
        if rect_carta.collidepoint(mouse_pos):
            return i
    return None


#BLOQUE PRINCIPAL

ejecutando = True
cartas_seleccionadas = []
posibles_indices_acertados = []
cartas_reveladas = []


while ejecutando:

    # DIBUJA LA PANTALLA
    for i, carta in enumerate(cartas):
        fila, columna = divmod(i, 4)  # Ahora tenemos 4 columnas
        x, y = columna * 100, fila * 150  # Espaciado entre cartas
        carta.dibujar((x, y))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if len(cartas_seleccionadas) < 2:
                indice = obtener_indice_carta_clic(evento.pos)
                posibles_indices_acertados.append(indice)
        
                if indice is not None and indice not in cartas_seleccionadas:
                    cartas_seleccionadas.append(cartas[indice].id_get())

                   
                    cartas[indice].voltear()

                    if len(cartas_seleccionadas) == 2:
                        if cartas_seleccionadas[0] == cartas_seleccionadas[1]:
                            
                            print("Iguales")
                            cartas_reveladas.extend(posibles_indices_acertados)
                            
                           
            else:

    
                count_aux = 0
                for carta in cartas:
                    if count_aux not in cartas_reveladas:
                        carta.volteada = False
                    count_aux+=1

                print(len(cartas_reveladas))
                if len(cartas_reveladas) >= 12:
                    print("GANASTE")
                    break

                cartas_seleccionadas = []
                posibles_indices_acertados = []


    
    
        
    

    pygame.display.flip()

# Salir del juego
pygame.quit()