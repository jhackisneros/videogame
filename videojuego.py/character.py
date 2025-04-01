class character:
    def __init__(self, x, y, image, health):
        super().__init__(x, y, image)
        self.health = health
    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
