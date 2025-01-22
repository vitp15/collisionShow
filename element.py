from config import *
import random
import pygame

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

class Element:
	images = [None, None, None]
	sound = [None, None, None]
	id: int
	radius: float
	x: float
	y: float
	dx: float
	dy: float
	
	def __init__(self, id: int, x_min: float, x_max: float, y_min: float, y_max: float, radius: float = RADIUS,
			  dx_min: float = -1, dx_max: float = 1, dy_min: float = -1, dy_max: float = 1):
		self.id = id
		self.radius = radius
		self.x = random.uniform(x_min + self.radius, x_max - self.radius)
		self.y = random.uniform(y_min + self.radius, y_max - self.radius)
		dx = random.uniform(dx_min, dx_max)
		dy = random.uniform(dy_min, dy_max)
		# normalize
		norm = (dx ** 2 + dy ** 2) ** 0.5
		self.dx = dx / norm
		self.dy = dy / norm

	def move(self):
		self.x += self.dx
		self.y += self.dy

		if self.x < 0 + self.radius or self.x > WIDTH - self.radius:
			self.dx *= -1
		if self.y < 0 + self.radius or self.y > SIMULATION_HEIGHT - self.radius:
			self.dy *= -1

	def draw(self, screen):
		for i in range(len(Element.images)):
			if i == self.id:
				if Element.images[i] is not None:
					screen.blit(Element.images[i], (int(self.x - self.radius), int(self.y - self.radius)))
				else:
					pygame.draw.circle(screen, COLORS[i], (int(self.x), int(self.y)), self.radius)
				break

	def transform(self, id):
		self.id = id
		for i in range(len(Element.sound)):
			if i == self.id and Element.sound[i] is not None:
				Element.sound[i].play()
				break

	def collision(self, other):
		return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.radius + other.radius) ** 2
	
def set_natural():
	Element.images = [FIRE_IMG, LEAF_IMG, WATER_IMG]
	Element.sound = [FIRE_SOUND, LEAF_SOUND, WATER_SOUND]

def set_animals():
	Element.images = [ELEPHANT_IMG, CAT_IMG, MOUSE_IMG]
	Element.sound = [ELEPHANT_SOUND, CAT_SOUND, MOUSE_SOUND]

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
