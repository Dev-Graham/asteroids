import pygame
import sys

BLACK = (0, 0, 0)
from constants import *

print("Screen width:", SCREEN_WIDTH)
print("Screen height:", SCREEN_HEIGHT)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
	print("Starting asteroids!")

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
	
		screen.fill(BLACK)

		pygame.display.flip()

	pygame.quit()
	sys.exit()


if __name__ == "__main__":
    main()
