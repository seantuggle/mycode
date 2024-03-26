import random

# Generate a random integer between a specified range
random_number = random.randint(1, 100)
print("Random integer between 1 and 100:", random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random floating-point number between 0 and 1:", random_float)

# Generate a random floating-point number within a specified range
random_float_range = random.uniform(1.5, 5.5)
print("Random floating-point number between 1.5 and 5.5:", random_float_range)

# Generate a random integer from a range with a specified step
random_step = random.randrange(0, 10, 2)  # Generate even numbers between 0 and 10
print("Random integer with a step of 2 between 0 and 10:", random_step)

# Shuffle a list randomly
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)

