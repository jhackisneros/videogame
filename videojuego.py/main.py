import pygame
import random

import opponent
import character
import entity
import player


# Main game loop
def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Opponent Example")

    clock = pygame.time.Clock()
    opponents = []
    spawn_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_event, 4000)  # Spawn an opponent every 4 seconds

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == spawn_event:
                # Spawn an opponent at a random edge of the screen
                edge = random.choice(['top', 'bottom', 'left', 'right'])
                if edge == 'top':
                    x, y = random.randint(0, screen_width), 0
                elif edge == 'bottom':
                    x, y = random.randint(0, screen_width), screen_height
                elif edge == 'left':
                    x, y = 0, random.randint(0, screen_height)
                else:  # 'right'
                    x, y = screen_width, random.randint(0, screen_height)

                opponent = opponent(name="Enemy", health=100, x=x, y=y)
                opponents.append(opponent)

        screen.fill((0, 0, 0))  # Clear the screen with black

        for opponent in opponents:
            opponent.move_towards_center(screen_width, screen_height)
            opponent.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()