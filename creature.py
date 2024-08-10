import random

class CreatureDNA:
    nucleotides = ['A', 'G', 'T', 'C']

    def __init__(self):
        self.attack_rgb, self.attack = self.random_attribute_and_value()
        self.health_rgb, self.health = self.random_attribute_and_value()
        self.defense_rgb, self.defense = self.random_attribute_and_value()
        self.age = self.random_attribute()
        self.speed = self.random_attribute()
        self.sight_range = self.random_attribute()
        self.weight_move = self.random_attribute()
        self.weight_attack = self.random_attribute()
        self.weight_eat = self.random_attribute()

        self.sequence = self.generate_dna_sequence()

    def random_attribute_and_value(self):
        # Generates a random 4-nucleotide sequence and returns the corresponding integer value
        nucleotide_sequence = ''.join(random.choice(self.nucleotides) for _ in range(4))
        value = self.agtc_to_value(nucleotide_sequence)
        return nucleotide_sequence, value

    def random_attribute(self):
        # Generates a random four nucleotide sequence
        return ''.join(random.choice(self.nucleotides) for _ in range(4))

    def agtc_to_value(self, agtc):
        # Converts a four nucleotide AGTC sequence into a value (0-255)
        mapping = {'A': 0, 'G': 1, 'T': 2, 'C': 3}
        value = 0
        for nucleotide in agtc:
            value = value * 4 + mapping[nucleotide]
        return value

    def generate_dna_sequence(self):
        # Generates the complete AGTC sequence for the creature
        return (
            self.attack_rgb +
            self.health_rgb +
            self.defense_rgb +
            self.age +
            self.speed +
            self.sight_range +
            self.weight_move +
            self.weight_attack +
            self.weight_eat
        )

    def __str__(self):
        # Returns a readable representation of the creature's DNA
        return (f"Attack (RGB): {self.attack_rgb} (Value: {self.attack}), "
                f"Health (RGB): {self.health_rgb} (Value: {self.health}), "
                f"Defense (RGB): {self.defense_rgb} (Value: {self.defense}), "
                f"Age: {self.age}, Speed: {self.speed}, Sight Range: {self.sight_range}, "
                f"Weight Move: {self.weight_move}, Weight Attack: {self.weight_attack}, Weight Eat: {self.weight_eat}, "
                f"Complete Sequence: {self.sequence}")

creature = CreatureDNA()
print(creature)
