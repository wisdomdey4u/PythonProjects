import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1 Option
print(random.choice(friends))

# 2 Option
random_index = random.randint(0,4)
print(friends[random_index])