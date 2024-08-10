import random
import pygame
import numpy as np
from creature import CreatureDNA
from quadtree import Quadtree
import cProfile
import pstats
import os

def profile_script(script_name):
    # Run the script with cProfile
    profiler = cProfile.Profile()
    profiler.enable()
    
    # Execute the script
    with open(script_name, 'rb') as f:
        exec(compile(f.read(), script_name, 'exec'))
    
    profiler.disable()
    
    # Print the profiling results
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative').print_stats(10)  # Change the number to show more or fewer lines

if __name__ == "__main__":
    # Replace 'main.py' with the path to your main script if it's in a different directory
    script_name = 'main.py'
    profile_script(script_name)
