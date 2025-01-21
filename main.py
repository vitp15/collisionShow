from config import *
import pygame
from element import Element, NatureElement, process_elements

def main():
	clock = pygame.time.Clock()
	running = True

	num_elements = 25
	fires = [NatureElement(0, 0, WIDTH / 3, 0, HEIGHT / 3) for _ in range(num_elements)]
	leafs = [NatureElement(1, 2 * WIDTH / 3, WIDTH, 0, HEIGHT / 3) for _ in range(num_elements)]
	waters = [NatureElement(2, WIDTH / 2 - WIDTH / 6, WIDTH / 2 + WIDTH / 6, 2 * HEIGHT / 3, HEIGHT) for _ in range(num_elements)]

	while running:
		screen.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		process_elements(fires, leafs, waters)
		process_elements(waters, fires, leafs)
		process_elements(leafs, waters, fires)

		pygame.display.flip()
		clock.tick(60)
	pygame.quit()

if __name__ == "__main__":
	main()
