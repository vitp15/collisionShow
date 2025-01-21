from config import *
import pygame
from element import Element, NatureElement, process_elements

def show_count(elements: list[Element]):
	font = pygame.font.Font(None, 36)
	count_screen.fill((0, 0, 0))
	count = [0, 0, 0]
	for element in elements:
		count[element.id] += 1
	fire_text = font.render(f": {count[0]}", True, (255, 255, 255))
	leaf_text = font.render(f": {count[1]}", True, (255, 255, 255))
	water_text = font.render(f": {count[2]}", True, (255, 255, 255))

	count_screen.blit(LEAF_IMG, (int(WIDTH / 2 - RADIUS), int(DISPLAY_HEIGHT / 2 - RADIUS)))
	count_screen.blit(FIRE_IMG, (int(WIDTH / 2 - WIDTH / 3 - RADIUS), int(DISPLAY_HEIGHT / 2 - RADIUS)))
	count_screen.blit(WATER_IMG, (int(WIDTH / 2 + WIDTH / 3 - RADIUS), int(DISPLAY_HEIGHT / 2 - RADIUS)))
	count_screen.blit(fire_text, (int(WIDTH / 2 - WIDTH / 3 + 2 * RADIUS), int(DISPLAY_HEIGHT / 2 - RADIUS / 2)))
	count_screen.blit(leaf_text, (int(WIDTH / 2 + 2 * RADIUS), int(DISPLAY_HEIGHT / 2 - RADIUS / 2)))
	count_screen.blit(water_text, (int(WIDTH / 2 + WIDTH / 3 + 2 * RADIUS), int(DISPLAY_HEIGHT / 2 - RADIUS / 2)))

def main():
	clock = pygame.time.Clock()
	running = True

	num_elements = 20
	fires = [NatureElement(0, 0, WIDTH / 3, 0, SIMULATION_HEIGHT / 3) for _ in range(num_elements)]
	leafs = [NatureElement(1, 2 * WIDTH / 3, WIDTH, 0, SIMULATION_HEIGHT / 3) for _ in range(num_elements)]
	waters = [NatureElement(2, WIDTH / 2 - WIDTH / 6, WIDTH / 2 + WIDTH / 6, 2 * SIMULATION_HEIGHT / 3, SIMULATION_HEIGHT) for _ in range(num_elements)]

	time.sleep(1)
	while running:
		simulation_screen.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		process_elements(fires, leafs, waters)
		process_elements(waters, fires, leafs)
		process_elements(leafs, waters, fires)
		show_count(fires + leafs + waters)

		pygame.display.flip()
		clock.tick(60)
	pygame.quit()

if __name__ == "__main__":
	main()
