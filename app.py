import sys
import os
import pygame
import random
import time
import glob
from PIL import Image
from win32.win32api import GetSystemMetrics

def main():
    # Center the Screen
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Get screen resolution
    screen_resolution = [int(GetSystemMetrics(0)), int(GetSystemMetrics(1))]
    screen_offset = [0, 0]

    # Reset screen after 300 Images drawn
    screen_reset = 300

    # Read jpg images from the /image direcotry 
    image_list = []
    for image_file in glob.glob("image/*.jpg"):
        image_list.append(image_file)

    # Initialize PygGame
    pygame.init()
    screen = pygame.display.set_mode(screen_resolution, pygame.NOFRAME)
    pygame.display.set_caption("Screensaver Image")
    pygame.mouse.set_visible(False)

    # Initialize Clock
    clock = pygame.time.Clock()

    # Set first screen background
    screen.fill((0, 136, 255))

    running = True
    while running:
        # Limit FPS to 4
        clock.tick(4)

        # Check for reset fill screen
        screen_reset -= 1
        if screen_reset <= 0:
            # Draw a rect over all to make a blur effect
            blur_surface = pygame.Surface((screen_resolution[0], screen_resolution[1]))
            blur_color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            for alpha in range(100):
                blur_surface.set_alpha(alpha)
                blur_surface.fill(blur_color)
                screen.blit(blur_surface, (0, 0))
                pygame.display.flip()
            screen_reset = 300

        # Select Random Image from List
        image_index = random.randrange(len(image_list))

        # Load Image per Pygame.Image.Load
        image_py_loaded = pygame.image.load(image_list[image_index])
        image_py_rect = image_py_loaded.get_rect()

        # Allow Pictures to be offset to top, left, right and bottom
        screen_offset[0] = random.randint(-100, screen_resolution[0] - image_py_rect[2] + 100)
        screen_offset[1] = random.randint(-100, screen_resolution[1] - image_py_rect[3] + 100)
        
        # Set Random x and y position of the image
        image_py_rect[0] = screen_offset[0]
        image_py_rect[1] = screen_offset[1]

        # Draw image to screen
        screen.blit(image_py_loaded, image_py_rect)

        # Display screen content
        pygame.display.flip()


        ### For closing the window # Don't change anything beyond this line ###
        for event in pygame.event.get():
            # Close game if a pygame.QUIT event is in queue
            if event.type == pygame.QUIT:
                running = False 

            # Close game if ESC is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT)) 

if __name__ == '__main__':
    main()
