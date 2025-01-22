import pygame
import random
import time

WIDTH, DISPLAY_HEIGHT, SIMULATION_HEIGHT = 600, 100, 600
BORDER = 7
RADIUS = 18

random.seed(time.time())

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, DISPLAY_HEIGHT + SIMULATION_HEIGHT + BORDER))
pygame.display.set_caption("Collision Show")

count_screen = screen.subsurface((0, 0, WIDTH, DISPLAY_HEIGHT))
simulation_screen = screen.subsurface((0, DISPLAY_HEIGHT + BORDER, WIDTH, SIMULATION_HEIGHT))

screen.fill((204, 204, 204))

FIRE_IMG = pygame.image.load("images/fire.png") 
LEAF_IMG = pygame.image.load("images/leaf.png")
WATER_IMG = pygame.image.load("images/water.png")

FIRE_IMG = pygame.transform.scale(FIRE_IMG, (2 * RADIUS, 2 * RADIUS))
LEAF_IMG = pygame.transform.scale(LEAF_IMG, (2 * RADIUS, 2 * RADIUS))
WATER_IMG = pygame.transform.scale(WATER_IMG, (2 * RADIUS, 2 * RADIUS))

MOUSE_IMG = pygame.image.load("images/mouse.png")
CAT_IMG = pygame.image.load("images/cat.png")
ELEPHANT_IMG = pygame.image.load("images/elephant.png")

MOUSE_IMG = pygame.transform.scale(MOUSE_IMG, (2 * 20, 2 * 20))
CAT_IMG = pygame.transform.scale(CAT_IMG, (2 * 25, 2 * 25))
ELEPHANT_IMG = pygame.transform.scale(ELEPHANT_IMG, (2 * 30, 2 * 30))

FIRE_SOUND = pygame.mixer.Sound("audio/fire.mp3")
LEAF_SOUND = pygame.mixer.Sound("audio/leaf.mp3")
WATER_SOUND = pygame.mixer.Sound("audio/water.mp3")

MOUSE_SOUND = pygame.mixer.Sound("audio/mouse.mp3")
CAT_SOUND = pygame.mixer.Sound("audio/cat.mp3")
ELEPHANT_SOUND = pygame.mixer.Sound("audio/elephant.mp3")
