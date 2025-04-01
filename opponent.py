from character import Character

class Opponent(Character):
    def __init__(self, name, health, is_star=False):
        super().__init__(name, health)
        self.is_star = is_star

    def move(self, direction):
        """
        Moves the opponent in the specified direction.
        :param direction: str - The direction to move (e.g., 'up', 'down', 'left', 'right').
        """
        print(f"{self.name} moves {direction}.")

    def shoot(self):
        """
        Makes the opponent shoot.
        """
        print(f"{self.name} shoots!")