import random

class CreatureDNA:
    nucleotides = ['A', 'G', 'T', 'C']

    def __init__(self):
        # Basic Attributes
        self.attack_rgb, self.attack = self.random_attribute_and_value()
        self.health_rgb, self.health = self.random_attribute_and_value()
        self.defense_rgb, self.defense = self.random_attribute_and_value()
        
        # Behavioral Genes
        self.speed = self.random_attribute_and_value()[1]
        self.movement_strategy = self.random_attribute()
        self.aggression_level = self.random_attribute()

        # Decision-Making Genes
        self.food_threshold = self.random_attribute() 
        self.flee_threshold = self.random_attribute()
        self.prioritization = self.random_attribute()

        # Reproduction and Energy Attributes
        self.reproduction_energy_threshold = random.randint(150, 255)
        self.reproduction_cost = random.randint(100, 200)
        self.energy_loss_rate = self.random_attribute_and_value()[1]
        self.max_age = self.random_attribute_and_value()[1]

        # Strategy and Learning
        self.learning_rate = self.random_attribute()
        self.memory = self.random_attribute()

        self.sequence = self.generate_dna_sequence()

    def random_attribute_and_value(self):
        # Generates a random four nucleotide sequence and returns the corresponding integer value
        nucleotide_sequence = ''.join(random.choice(self.nucleotides) for _ in range(4))
        value = self.agtc_to_value(nucleotide_sequence)
        return nucleotide_sequence, value

    def random_attribute(self):
        # Generates a random four nucleotide sequence
        return ''.join(random.choice(self.nucleotides) for _ in range(4))

    def agtc_to_value(self, agtc):
        # Converts a four nucleotide AGTC sequence into an int (0-255)
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
            self.movement_strategy +
            self.aggression_level +
            self.random_attribute() +  # Placeholder
            self.random_attribute() +  # Placeholder
            self.learning_rate +
            self.memory +
            self.random_attribute() +  # Placeholder
            self.random_attribute() +  # Placeholder
            self.random_attribute()    # Placeholder
        )

    def __str__(self):
        # Returns a readable representation of the creature's DNA
        return (f"Attack (RGB): {self.attack_rgb} (Value: {self.attack}), "
                f"Health (RGB): {self.health_rgb} (Value: {self.health}), "
                f"Defense (RGB): {self.defense_rgb} (Value: {self.defense}), "
                f"Speed: {self.speed}, Reproduction Energy Threshold: {self.reproduction_energy_threshold}, "
                f"Reproduction Cost: {self.reproduction_cost}, Energy Loss Rate: {self.energy_loss_rate}, Max Age: {self.max_age}, "
                f"Movement Strategy: {self.movement_strategy}, Aggression Level: {self.aggression_level}, "
                f"Learning Rate: {self.learning_rate}, Memory: {self.memory}, "
                f"Complete Sequence: {self.sequence}")

creature = CreatureDNA()
print(creature)
