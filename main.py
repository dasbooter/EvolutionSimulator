import pygame
import random
import numpy as np
from creature import CreatureDNA
from quadtree import Quadtree

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

# Population and food settings
population = 25
initial_food = 10
food_generation_rate = 0.1  # Per frame
creature_radius = 5 

creatures = []
for _ in range(population):
    creature = CreatureDNA()
    # Generate a random position for each creature
    pos = np.array([random.randrange(10, 1910), random.randrange(10, 1070)], dtype=float)
    # Extract RGB values from the creature's DNA
    color = (creature.attack, creature.health, creature.defense)
    creatures.append({"pos": pos, "dna": creature, "color": color, "energy": 100, "age": 0})

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

# Ensure creatures do not overlap
def avoid_collision(pos, creature_radius, quadtree):
    range_rect = (pos[0] - creature_radius, pos[1] - creature_radius, creature_radius * 2, creature_radius * 2)
    nearby_creatures = []
    quadtree.query(range_rect, nearby_creatures)

    for other_creature in nearby_creatures:
        if other_creature["pos"] is not pos:
            distance = np.linalg.norm(other_creature["pos"] - pos)
            if distance < 2 * creature_radius:
                direction = pos - other_creature["pos"]
                direction = direction / np.linalg.norm(direction)
                pos += direction * (2 * creature_radius - distance)
    return pos

def reproduce(creature, creatures, creature_radius):
    # Offspring inherits DNA with potential mutation
    parent_dna = creature["dna"]
    new_dna = CreatureDNA()

    # Mutate attributes with a small chance
    mutation_chance = 0.05
    if random.random() < mutation_chance:
        new_dna.speed = max(0, min(255, parent_dna.speed + random.randint(-10, 10)))
    else:
        new_dna.speed = parent_dna.speed

    # Inherit reproduction attributes with possible mutation
    for attr in ['reproduction_energy_threshold', 'reproduction_cost', 'energy_loss_rate', 'max_age']:
        setattr(new_dna, attr, max(0, min(255, getattr(parent_dna, attr) + random.randint(-5, 5))))

    # Place the offspring near the parent but not overlapping
    offset = np.random.normal(0, 10, 2)
    new_pos = creature["pos"] + offset
    color = (new_dna.attack, new_dna.health, new_dna.defense)
    creatures.append({"pos": new_pos, "dna": new_dna, "color": color, "energy": 50, "age": 0})
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    add_food(food_positions, food_generation_rate)

    for pos in food_positions:
        pygame.draw.circle(screen, "green", pos.astype(int), 2)

    quadtree = Quadtree((0, 0, screen.get_width(), screen.get_height()), capacity=4)
    for creature in creatures:
        quadtree.insert(creature)

    new_creatures = []
    for creature in creatures:
        pos = creature["pos"]
        dna = creature["dna"]
        speed = dna.speed / 64.0
        energy = creature["energy"]
        age = creature["age"]

        creature["age"] += 1

        if food_positions:
            food_distances = np.linalg.norm(np.array(food_positions) - pos, axis=1)
            nearest_food_idx = np.argmin(food_distances)
            nearest_food = food_positions[nearest_food_idx]

            new_pos = move_towards(nearest_food, pos, speed)
            creature["pos"] = new_pos

            if np.linalg.norm(new_pos - nearest_food) < 5:
                food_positions.pop(nearest_food_idx)
                energy += 50
                creature["energy"] = energy

        energy -= dna.energy_loss_rate / 100.0
        creature["energy"] = energy

        if energy > dna.reproduction_energy_threshold and age < dna.max_age:
            reproduce(creature, new_creatures, creature_radius)
            energy -= dna.reproduction_cost

        creature["pos"] = avoid_collision(creature["pos"], creature_radius, quadtree)

        if energy > 0 and age < dna.max_age:
            new_creatures.append(creature)

        pygame.draw.circle(screen, creature["color"], creature["pos"].astype(int), creature_radius)

    creatures = new_creatures

    pygame.display.flip()
    clock.tick(60)

pygame.quit()