import random
import matplotlib.pyplot as plt
random_integer = [random.randint(1,100) for _ in range(100)]
plt.hist(random_integer)
plt.xlabel("Random Integers")
plt.ylabel("Value Ranges")
plt.show()