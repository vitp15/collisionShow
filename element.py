from config import *
import random
import pygame

class Element:
	id: int
	radius: float
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
		if self.y < 0 + RADIUS or self.y > SIMULATION_HEIGHT - RADIUS:
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
		if self.id == 0:
			fire_sound.play()
		elif self.id == 1:
			leaf_sound.play()
		else:
			water_sound.play()

	def collision(self, other):
		return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (2 * RADIUS) ** 2
	
class NatureElement(Element):
	def draw(self, screen):
		if self.id == 0:
			screen.blit(FIRE_IMG, (int(self.x - RADIUS), int(self.y - RADIUS)))
		elif self.id == 1:
			screen.blit(LEAF_IMG, (int(self.x - RADIUS), int(self.y - RADIUS)))
		else:
			screen.blit(WATER_IMG, (int(self.x - RADIUS), int(self.y - RADIUS)))

def process_elements(elements: list[Element], weakers: list[Element], strongers: list[Element]):
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
		element.draw(simulation_screen)
