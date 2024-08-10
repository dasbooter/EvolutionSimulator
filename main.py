import pygame
import random
import numpy as np
from creature import CreatureDNA

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

# Population and food settings
population = 50
initial_food = 25
food_generation_rate = 0.1  # Per frame

creatures = []
for _ in range(population):
    creature = CreatureDNA()
    # Generate a random position for each creature
    pos = np.array([random.randrange(10, 1910), random.randrange(10, 1070)], dtype=float)
    # Extract RGB values from the creature's DNA
    color = (creature.attack, creature.health, creature.defense)
    creatures.append({"pos": pos, "dna": creature, "color": color, "energy": 100})

food_positions = []
for _ in range(initial_food):
    pos = np.array([random.randrange(10, 1910), random.randrange(10, 1070)], dtype=float)
    food_positions.append(pos)

def move_towards(target, position, speed):
    # Move from the current position towards a target position
    direction = target - position
    distance = np.linalg.norm(direction)
    if distance > 0:
        direction = direction / distance
        position += direction * speed
    return position

def add_food(food_positions, food_generation_rate):
    # Add food to the environment gradually 
    if random.random() < food_generation_rate:
        new_food_pos = np.array([random.randrange(10, 1910), random.randrange(10, 1070)], dtype=float)
        food_positions.append(new_food_pos)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # Gradually add new food to the environment
    add_food(food_positions, food_generation_rate)

    # Draw food
    for pos in food_positions:
        pygame.draw.circle(screen, "green", pos.astype(int), 2)

    # Update and draw creatures
    for creature in creatures:
        pos = creature["pos"]
        dna = creature["dna"]
        speed = dna.speed / 64.0
        energy = creature["energy"]

        if food_positions:  # Only proceed if there is food available
            # Find the nearest food
            food_distances = np.linalg.norm(np.array(food_positions) - pos, axis=1)
            nearest_food_idx = np.argmin(food_distances)
            nearest_food = food_positions[nearest_food_idx]

            # Move towards the nearest food
            new_pos = move_towards(nearest_food, pos, speed)
            creature["pos"] = new_pos

            # Check if the creature has reached the food
            if np.linalg.norm(new_pos - nearest_food) < 5:
                food_positions.pop(nearest_food_idx)
                energy += 50
                creature["energy"] = energy

        # Draw the creature
        pygame.draw.circle(screen, creature["color"], new_pos.astype(int), 5)

    # Display update
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
