import pygame
import random
import time

WIDTH, DISPLAY_HEIGHT, SIMULATION_HEIGHT = 600, 100, 600
BORDER = 7
RADIUS = 18

FIRE_IMG = pygame.image.load("images/fire.png") 
LEAF_IMG = pygame.image.load("images/leaf.png")
WATER_IMG = pygame.image.load("images/water.png")

FIRE_IMG = pygame.transform.scale(FIRE_IMG, (2 * RADIUS, 2 * RADIUS))
LEAF_IMG = pygame.transform.scale(LEAF_IMG, (2 * RADIUS, 2 * RADIUS))
WATER_IMG = pygame.transform.scale(WATER_IMG, (2 * RADIUS, 2 * RADIUS))

pygame.init()
screen = pygame.display.set_mode((WIDTH, DISPLAY_HEIGHT + SIMULATION_HEIGHT + BORDER))
pygame.display.set_caption("Collision Show")

count_screen = screen.subsurface((0, 0, WIDTH, DISPLAY_HEIGHT))
simulation_screen = screen.subsurface((0, DISPLAY_HEIGHT + BORDER, WIDTH, SIMULATION_HEIGHT))

screen.fill((204, 204, 204))

pygame.mixer.init()
fire_sound = pygame.mixer.Sound("audio/fire.mp3")
leaf_sound = pygame.mixer.Sound("audio/leaf.mp3")
water_sound = pygame.mixer.Sound("audio/water.mp3")

random.seed(time.time())
