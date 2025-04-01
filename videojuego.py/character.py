from entity import entity  # Importa la clase entity

class character(entity):  # Hereda de entity
    def __init__(self, x, y, image, health):
        super().__init__(x, y, image)  # Llama al constructor de entity
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0