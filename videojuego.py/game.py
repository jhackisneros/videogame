class Game:
    def __init__(self, title, width, height):
        """
        Inicializa el juego con un título, ancho y alto de la ventana.
        """
        self.title = title
        self.width = width
        self.height = height
        self.running = False

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

    def handle_events(self):
        """
        Maneja los eventos del juego (entrada del usuario, etc.).
        """
        pass

    def update(self):
        """
        Actualiza la lógica del juego.
        """
        pass

    def render(self):
        """
        Renderiza los elementos del juego en pantalla.
        """
        pass