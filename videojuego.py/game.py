import time

class Game:
    def __init__(self, title, width, height):
        """
        Inicializa el juego con un título, ancho y alto de la ventana.
        """
        self.title = title
        self.width = width
        self.height = height
        self.running = False
        self.frame_count = 0  # Contador de fotogramas

    def start(self):
        """
        Inicia el bucle principal del juego.
        """
        self.running = True
        print(f"{self.title} ha comenzado.")
        self.game_loop()

    def stop(self):
        """
        Detiene el juego.
        """
        self.running = False
        print(f"{self.title} ha terminado.")

    def game_loop(self):
        """
        Bucle principal del juego.
        """
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            time.sleep(1 / 60)  # Simula 60 FPS

    def handle_events(self):
        """
        Maneja los eventos del juego (entrada del usuario, etc.).
        """
        user_input = input("Presiona 'q' para salir: ").strip().lower()
        if user_input == 'q':
            self.stop()

    def update(self):
        """
        Actualiza la lógica del juego.
        """
        self.frame_count += 1
        print(f"Actualizando lógica del juego. Fotograma: {self.frame_count}")

    def render(self):
        """
        Renderiza los elementos del juego en pantalla.
        """
        print(f"Renderizando el juego en {self.width}x{self.height}. Fotograma: {self.frame_count}")