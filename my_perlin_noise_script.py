import noise
import numpy as np

size = 16
scale = 10.0
octaves = 6
persistence = 0.5
lacunarity = 2.0

world = np.zeros(size)
min_val = float('inf')
max_val = float('-inf')

for i in range(size):
    n = noise.pnoise1(i / scale, 
                      octaves=octaves, 
                      persistence=persistence, 
                      lacunarity=lacunarity, 
                      repeat=1024, 
                      base=42)
    world[i] = n
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n

world = (world - min_val) / (max_val - min_val)

sorted_world = np.sort(world)

for i in range(size):
    print(f"Index {i}: {sorted_world[i]:.4f}")