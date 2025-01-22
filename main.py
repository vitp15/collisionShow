from config import *
import pygame
from element import *

TEXT_COLOR = (255, 255, 255)
elements_to_show: list[Element] = [None, None, None]

def show_count(elements: list[Element]):
	font = pygame.font.Font(None, 36)
	count_screen.fill((0, 0, 0))
	count = [0, 0, 0]
	for element in elements:
		count[element.id] += 1
		if elements_to_show[element.id] is None:
			elements_to_show[element.id] = Element(element.id, 0, 0, 0, 0, element.radius)
			elements_to_show[element.id].x = WIDTH / 2 + (element.id - 1) * WIDTH / 3
			elements_to_show[element.id].y = DISPLAY_HEIGHT / 2
	first_text = font.render(f": {count[0]}", True, TEXT_COLOR)
	second_text = font.render(f": {count[1]}", True, TEXT_COLOR)
	third_text = font.render(f": {count[2]}", True, TEXT_COLOR)

	for elment_to_show in elements_to_show:
		if elment_to_show is not None:
			elment_to_show.draw(count_screen)

	count_screen.blit(first_text, (int(WIDTH / 2 - WIDTH / 3 + 2 * elements_to_show[0].radius), int(DISPLAY_HEIGHT / 2 - elements_to_show[0].radius / 2)))
	count_screen.blit(second_text, (int(WIDTH / 2 + 2 * elements_to_show[1].radius), int(DISPLAY_HEIGHT / 2 - elements_to_show[1].radius / 2)))
	count_screen.blit(third_text, (int(WIDTH / 2 + WIDTH / 3 + 2 * elements_to_show[2].radius), int(DISPLAY_HEIGHT / 2 - elements_to_show[2].radius / 2)))

def main():
	clock = pygame.time.Clock()
	running = True

	num_elements = 7
	set_animals()
	first = [Element(0, 0, WIDTH / 3, 0, SIMULATION_HEIGHT / 3, radius=30) for _ in range(num_elements)]
	second = [Element(1, 2 * WIDTH / 3, WIDTH, 0, SIMULATION_HEIGHT / 3, radius=25) for _ in range(num_elements)]
	third = [Element(2, WIDTH / 2 - WIDTH / 6, WIDTH / 2 + WIDTH / 6, 2 * SIMULATION_HEIGHT / 3, SIMULATION_HEIGHT, radius=20) for _ in range(num_elements)]

	time.sleep(1)
	while running:
		simulation_screen.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		process_elements(first, second, third)
		process_elements(third, first, second)
		process_elements(second, third, first)
		show_count(first + second + third)

		pygame.display.flip()
		clock.tick(60)
	pygame.quit()

if __name__ == "__main__":
	main()
