#Librerias
import pygame # Libreria requerida como requerimiento.
import random # para mezclar una lista.
import os # para centrar ventana.
import copy #para copiar objetos.
import subprocess # para abrir otro archivo .py

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 255)


# Configuración de la ventana , colores y fuentes.
pygame.init()
WIDTH, HEIGHT = 400, 600
fondo = pygame.image.load("wall2.png")
fondo = pygame.transform.scale(fondo, (WIDTH, HEIGHT))
pygame.display.set_caption("YuGiOh Memories")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(NEGRO)
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.mixer.music.load("soundtrack.mp3")

if not pygame.mixer.music.get_busy():
    pygame.mixer.music.play(-1)  # El valor -1 indica que la músic
    pygame.mixer.music.set_volume(0.2)

# Clase 'Carta'
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

# ASOCIAMOS LAS IMAGENES Y NOMBRE CON EL OBJETO DE LA CLASE 'Carta'
cartas = []
count = 0

for img in imagenes_cartas:
    cartas.extend([Carta(imagenes_cartas[img])])
    cartas[count].id_set(img)
    count += 1

# Añadimos mas cartas para que sean en total 12.
for i in range(len(cartas)):
    for j in range(3):
        cartas.append(copy.copy(cartas[i]))

# Mezclar la lista con las cartas ("Barajar")
random.shuffle(cartas)  

#Obtener datos de la carta clickeada.
def obtener_indice_carta_clic(mouse_pos):
    for i, carta in enumerate(cartas):
        fila, columna = divmod(i, 4)  # Cambia 4 por el número de columnas que desees
        x = columna * 100  # Espaciado horizontal entre cartas
        y = (fila * 150) + ((HEIGHT - (len(cartas) // 4) * 150) // 2)
        rect_carta = pygame.Rect(x, y, 100, 150)  # Rectángulo que representa la carta
        if rect_carta.collidepoint(mouse_pos):
            return i
    return None

#BLOQUE PRINCIPAL
ejecutando = True
cartas_seleccionadas = []
posibles_indices_acertados = []
cartas_reveladas = []

aux = 0

# Bucle principal
while ejecutando:
    # Dibujar cartas
    for i, carta in enumerate(cartas):
        fila, columna = divmod(i, 4)  # Ahora tenemos 4 columnas
        x = columna * 100  # Espaciado horizontal entre cartas
        y = (fila * 150) + ((HEIGHT - (len(cartas) // 4) * 150) // 2)  # Centrar verticalmente las cartas
        carta.dibujar((x, y))
    
    # Resto del código del bucle principal

    # Mientras que pygame este ejecutandose
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            aux +=1

            if len(cartas_seleccionadas) < 2:
                indice = obtener_indice_carta_clic(evento.pos)
                posibles_indices_acertados.append(indice)

                # Aqui añadimos la carta si no ah sido seleccionada antes y que no sea seleccion duplicada.
                if indice is not None and indice not in cartas_seleccionadas:
                    cartas_seleccionadas.append(cartas[indice].id_get())

                    # La mostramos
                    cartas[indice].voltear()
                    
                    # Revisamos si las dos cartas que selecionamos son iguales.
                    if len(cartas_seleccionadas) == 2:
                        if cartas_seleccionadas[0] == cartas_seleccionadas[1]: 

                            # Añadimos las cartas a la lista de cartas resueltas
                            cartas_reveladas.extend(posibles_indices_acertados)
                                   
            else:

                count_aux = 0

                #Ocultamos todas las cartas nuevamente excepto las que ya se resolvieron.

                for carta in cartas:
                    if count_aux not in cartas_reveladas:
                        carta.volteada = False
                    count_aux+=1


                # Verificamos cuantas cartas llevamos resueltas.
                if len(cartas_reveladas) >= 12:
                    ejecutando = False
                    subprocess.run(["python", "win.py"])
                   
                    

                # Reiniciamos las listas dado que los valores que contienen 
                # ya no son utiles dado que en este caso las 
                # cartas no son iguales y ya termino el 'turno'.
                cartas_seleccionadas = []
                posibles_indices_acertados = []
    

    pygame.display.flip()
    screen.blit(fondo, (0, 0))
    

# Salir del juego
pygame.quit()