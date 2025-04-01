from character import character

class player(character):
    def __init__(self, x, y, image, health, speed):
        super().__init__(x, y, image, health)
        self.speed = speed

    def move(self, dx, dy):
        super().move(dx * self.speed, dy * self.speed)

    def handle_input(self, key):
        if key == 'w':  # Move up
            self.move(0, -1)
        elif key == 's':  # Move down
            self.move(0, 1)
        elif key == 'a':  # Move left
            self.move(-1, 0)
        elif key == 'd':  # Move right
            self.move(1, 0)