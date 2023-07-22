import pygame
import sys
import random

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 300
GROUND_HEIGHT = 50
FPS = 60


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game")
clock = pygame.time.Clock()



dino_img = pygame.image.load("dino.png")
ground_img = pygame.image.load("ground.png")



dino_width, dino_height = 40, 40
dino_x, dino_y = 50, SCREEN_HEIGHT - GROUND_HEIGHT - dino_height
dino_vel_y = 0
dino_jump_power = -12
gravity = 1



ground_x, ground_y = 0, SCREEN_HEIGHT - GROUND_HEIGHT
ground_vel_x = -5



def main():
    global dino_y, dino_vel_y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dino_y == SCREEN_HEIGHT - GROUND_HEIGHT - dino_height:
                    dino_vel_y = dino_jump_power

        # Update dino's position and velocity
        dino_y += dino_vel_y
        dino_vel_y += gravity

        # Keep dino on the ground
        if dino_y >= SCREEN_HEIGHT - GROUND_HEIGHT - dino_height:
            dino_y = SCREEN_HEIGHT - GROUND_HEIGHT - dino_height
            dino_vel_y = 0

        # Update ground position
        ground_x += ground_vel_x
        if ground_x <= -SCREEN_WIDTH:
            ground_x = 0

        # Draw the game
        screen.fill((255, 255, 255))
        screen.blit(dino_img, (dino_x, dino_y))
        screen.blit(ground_img, (ground_x, ground_y))
        pygame.display.flip()
        clock.tick(FPS)

        if __name__ == "__main__":
                main()
import pygame
import sys
import random

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 300
GROUND_HEIGHT = 50
FPS = 60


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game")
clock = pygame.time.Clock()



dino_img = pygame.image.load("dino.png")
ground_img = pygame.image.load("ground.png")



dino_width, dino_height = 40, 40
dino_x, dino_y = 50, SCREEN_HEIGHT - GROUND_HEIGHT - dino_height
dino_vel_y = 0
dino_jump_power = -12
gravity = 1



ground_x, ground_y = 0, SCREEN_HEIGHT - GROUND_HEIGHT
ground_vel_x = -5



def main():
    global dino_y, dino_vel_y

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dino_y == SCREEN_HEIGHT - GROUND_HEIGHT - dino_height:
                    dino_vel_y = dino_jump_power

        # Update dino's position and velocity
        dino_y += dino_vel_y
        dino_vel_y += gravity

        # Keep dino on the ground
        if dino_y >= SCREEN_HEIGHT - GROUND_HEIGHT - dino_height:
            dino_y = SCREEN_HEIGHT - GROUND_HEIGHT - dino_height
            dino_vel_y = 0

        # Update ground position
        ground_x += ground_vel_x
        if ground_x <= -SCREEN_WIDTH:
            ground_x = 0

        # Draw the game
        screen.fill((255, 255, 255))
        screen.blit(dino_img, (dino_x, dino_y))
        screen.blit(ground_img, (ground_x, ground_y))
        pygame.display.flip()
        clock.tick(FPS)

        if __name__ == "__main__":
                main()
