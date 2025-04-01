import pygame
import random

from opponent import Opponent
from player import player


# Main game loop
def main():
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Playable Game")

    clock = pygame.time.Clock()
    opponents = []
    spawn_event = pygame.USEREVENT + 1
    pygame.time.set_timer(spawn_event, 4000)  # Spawn an opponent every 4 seconds

    # Create the player
    player_image = pygame.Surface((40, 40))  # Placeholder for player image
    player_image.fill((0, 255, 0))  # Green square
    player_obj = player(x=screen_width // 2, y=screen_height // 2, image=player_image, health=100, speed=5)

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

                new_opponent = Opponent(name="Enemy", health=100, x=x, y=y)
                opponents.append(new_opponent)

        # Handle player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # Move up
            player_obj.move(0, -1)
        if keys[pygame.K_s]:  # Move down
            player_obj.move(0, 1)
        if keys[pygame.K_a]:  # Move left
            player_obj.move(-1, 0)
        if keys[pygame.K_d]:  # Move right
            player_obj.move(1, 0)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Update and draw opponents
        for opponent in opponents:
            opponent.move_towards_player(player_obj.x, player_obj.y, player_obj.speed)
            opponent.draw(screen)

        # Draw the player
        player_obj.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()