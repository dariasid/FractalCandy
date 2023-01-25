import fractal
import random
import numpy as np
import matplotlib.pyplot as plt

def generate_fractal_candy():
    # Create a fractal object with random parameters
    f = fractal.Fractal(random.randint(3, 6), random.uniform(0.1, 0.9), random.uniform(0.1, 0.9))
    # Generate the fractal shape
    candy = f.generate()
    # Add noise to the fractal shape to make it look more like candy
    noise = np.random.normal(0, 0.05, candy.shape)
    candy = candy + noise
    candy = np.clip(candy, 0, 1)
    # Apply a candy-like color map to the fractal shape
    candy = plt.cm.YlOrBr(candy)
    # Return the fractal candy
    return candy

# Generate 10 fractal candy images
for i in range(10):
    candy = generate_fractal_candy()
    plt.imsave("fractal_candy_{}.png".format(i), candy)
