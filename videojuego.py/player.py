from character import character 

class player(character):
    def __init__(self, x, y, image, health, speed):
        super().__init__(x, y, image, health) 
        self.speed = speed

    def move(self, dx, dy):
        super().move(dx * self.speed, dy * self.speed) 