import pygame
import random
from character import Character

class Opponent:
    def __init__(self, name, health, x, y):
        self.name = name
        self.health = health
        self.x = x
        self.y = y
        self.speed = 2  # Base speed

    def move_towards_player(self, player_x, player_y, player_speed):
        # Enemies are 3 times slower than the player
        adjusted_speed = player_speed / 3

        if self.x < player_x:
            self.x += adjusted_speed
        elif self.x > player_x:
            self.x -= adjusted_speed
        if self.y < player_y:
            self.y += adjusted_speed
        elif self.y > player_y:
            self.y -= adjusted_speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 20)

