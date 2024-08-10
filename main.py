import pygame

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("green")
	#NumPy GOES HERE
	pygame.display.flip()
	clock.tick(60)
pygame.quit()

