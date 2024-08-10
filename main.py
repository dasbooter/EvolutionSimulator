import pygame
import random
from creature import CreatureDNA

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
pos = random.randrange(10, 1910), random.randrange(10, 1070)
population = 50
creatures = []

for _ in range(population):
    creature = CreatureDNA()
    # Generate a random position for each creature
    pos = random.randrange(10, 1910), random.randrange(10, 1070)
    # Extract RGB values from the creature's DNA
    color = (creature.attack, creature.health, creature.defense)
    creatures.append((pos, color))

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("black")
	for pos, color in creatures:
		pygame.draw.circle(screen, color, pos, 10)
	#NumPy goes here
	pygame.display.flip()
	clock.tick(60)
pygame.quit()

