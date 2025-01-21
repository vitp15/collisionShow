import pygame
import random
import time

WIDTH, HEIGHT = 500, 500
RADIUS = 15
MAX_ID = 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Show")

random.seed(time.time())

class Element:
	id: int
	x: float
	y: float
	dx: float
	dy: float
	
	def __init__(self, id: int, x_min: float, x_max: float, y_min: float, y_max: float,
			  dx_min: float = -1, dx_max: float = 1, dy_min: float = -1, dy_max: float = 1):
		self.id = id
		self.x = random.uniform(x_min + RADIUS, x_max - RADIUS)
		self.y = random.uniform(y_min + RADIUS, y_max - RADIUS)
		dx = random.uniform(dx_min, dx_max)
		dy = random.uniform(dy_min, dy_max)
		# normalize
		norm = (dx ** 2 + dy ** 2) ** 0.5
		self.dx = dx / norm
		self.dy = dy / norm

	def move(self):
		self.x += self.dx
		self.y += self.dy

		if self.x < 0 + RADIUS or self.x > WIDTH - RADIUS:
			self.dx *= -1
		if self.y < 0 + RADIUS or self.y > HEIGHT - RADIUS:
			self.dy *= -1

	def draw(self, screen):
		if self.id == 0:
			pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), RADIUS)
		elif self.id == 1:
			pygame.draw.circle(screen, (0, 255, 0), (int(self.x), int(self.y)), RADIUS)
		else:
			pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), RADIUS)

	def transform(self, id):
		self.id = id

	def collision(self, other):
		return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (2 * RADIUS) ** 2

def process_elements(elements: list, weakers: list, strongers: list):
	for element in elements.copy():
		element.move()
		for weaker in weakers.copy():
			if element.collision(weaker):
				weaker.transform(element.id)
				if weaker in weakers:
					weakers.remove(weaker)
				if not weaker in elements:
					elements.append(weaker)
		for stronger in strongers.copy():
			if element.collision(stronger):
				element.transform(stronger.id)
				if element in elements:
					elements.remove(element)
				if not element in strongers:
					strongers.append(element)
		element.draw(screen)

def main():
	clock = pygame.time.Clock()
	running = True

	num_elements = 20
	fires = [Element(0, 0, WIDTH / 3, 0, HEIGHT / 3) for _ in range(num_elements)]
	leafs = [Element(1, 2 * WIDTH / 3, WIDTH, 0, HEIGHT / 3) for _ in range(num_elements)]
	waters = [Element(2, WIDTH / 2 - WIDTH / 6, WIDTH / 2 + WIDTH / 6, 2 * HEIGHT / 3, HEIGHT) for _ in range(num_elements)]

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
