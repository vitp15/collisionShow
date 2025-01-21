import pygame
import random
import time

WIDTH, HEIGHT = 500, 500
RADIUS = 15
MAX_ID = 2

FIRE_IMG = pygame.image.load("images/fire.png") 
LEAF_IMG = pygame.image.load("images/leaf.png")
WATER_IMG = pygame.image.load("images/water.png")

FIRE_IMG = pygame.transform.scale(FIRE_IMG, (2 * RADIUS, 2 * RADIUS))
LEAF_IMG = pygame.transform.scale(LEAF_IMG, (2 * RADIUS, 2 * RADIUS))
WATER_IMG = pygame.transform.scale(WATER_IMG, (2 * RADIUS, 2 * RADIUS))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Show")

random.seed(time.time())
