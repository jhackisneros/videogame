import pygame
import random

# Inicializar pygame
pygame

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Monstruos")

# Cargar imágenes
background = pygame.image.load("assets/background.png")  # Imagen de fondo
monster_imgs = {
    "normal": pygame.image.load("assets/monster_normal.png"),
    "rapido": pygame.image.load("assets/monster_rapido.png"),
    "escudero": pygame.image.load("assets/monster_escudero.png"),
    "boss": pygame.image.load("assets/monster_boss.png")
}

# Escalar imágenes para que tengan el mismo tamaño
for key in monster_imgs:
    monster_imgs[key] = pygame.transform.scale(monster_imgs[key], (50, 50))


class Monstruo:
    def __init__(self, ataque, vida, destreza, x, y, velocidad, imagen):
        self.ataque = ataque
        self.vida = vida
        self.destreza = destreza
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.imagen = imagen

    def mover(self, dx, dy):
        """Mueve al monstruo dentro de los límites de la pantalla."""
        self.x = max(0, min(WIDTH - 50, self.x + dx * self.velocidad))
        self.y = max(0, min(HEIGHT - 50, self.y + dy * self.velocidad))

    def dibujar(self, screen):
        """Dibuja al monstruo en la pantalla."""
        screen.blit(self.imagen, (self.x, self.y))


class Normal(Monstruo):
    def __init__(self, x, y):
        super().__init__(ataque=50, vida=100, destreza=30, x=x, y=y, velocidad=2, imagen=monster_imgs["normal"])


class Rapido(Monstruo):
    def __init__(self, x, y):
        super().__init__(ataque=60, vida=80, destreza=40, x=x, y=y, velocidad=4, imagen=monster_imgs["rapido"])


class Escudero(Monstruo):
    def __init__(self, x, y):
        super().__init__(ataque=40, vida=120, destreza=20, x=x, y=y, velocidad=1, imagen=monster_imgs["escudero"])
        self.escudo = 30  # Tiene escudo adicional


class Boss1(Monstruo):
    def __init__(self, x, y):
        super().__init__(ataque=100, vida=300, destreza=50, x=x, y=y, velocidad=3, imagen=monster_imgs["boss"])
        self.escudo = 40
        self.rango = 60
        self.evasion = 25

    def mover(self, dx, dy):
        """El boss1 puede moverse erráticamente con su evasión."""
        evasion_extra = random.randint(-self.evasion, self.evasion)  # Se mueve de forma errática
        super().mover(dx + evasion_extra, dy + evasion_extra)


# Crear monstruos en diferentes posiciones
monstruos = [
    Normal(100, 100),
    Rapido(300, 200),
    Escudero(500, 400),
    Boss1(600, 100)
]

# Índice para controlar qué monstruo se mueve con las teclas
monstruo_jugador = 0  

# Bucle principal del juego
running = True
while running:
    pygame.time.delay(30)  # Controlar la velocidad del bucle

    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Cambiar de monstruo con la tecla TAB
            if event.key == pygame.K_TAB:
                monstruo_jugador = (monstruo_jugador + 1) % len(monstruos)

    # Detectar teclas presionadas para mover el monstruo seleccionado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        monstruos[monstruo_jugador].mover(-1, 0)
    if keys[pygame.K_RIGHT]:
        monstruos[monstruo_jugador].mover(1, 0)
    if keys[pygame.K_UP]:
        monstruos[monstruo_jugador].mover(0, -1)
    if keys[pygame.K_DOWN]:
        monstruos[monstruo_jugador].mover(0, 1)

    # Dibujar elementos en pantalla
    screen.blit(background, (0, 0))  # Fondo
    for monstruo in monstruos:
        monstruo.dibujar(screen)  # Dibujar cada monstruo

    pygame.display.update()  # Actualizar la pantalla

pygame.quit()
