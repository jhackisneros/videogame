import pygame
import random
from character import Character

class Opponent:
    def __init__(self, name, health, x, y):
        self.name = name
        self.health = health
        self.x = x
        self.y = y
        self.speed = 2

    def move_towards_center(self, screen_width, screen_height):
        center_x, center_y = screen_width // 2, screen_height // 2
        if self.x < center_x:
            self.x += self.speed
        elif self.x > center_x:
            self.x -= self.speed
        if self.y < center_y:
            self.y += self.speed
        elif self.y > center_y:
            self.y -= self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 20)

