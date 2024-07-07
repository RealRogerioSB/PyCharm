import matplotlib.pyplot as plt
import numpy as np

plt.style.use("_mpl-gallery-nogrid")

np.random.seed(1)
x = np.random.uniform(-3, 3, 256)
y = np.random.uniform(-3, 3, 256)
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

fig, ax = plt.subplots()

ax.triplot(x, y)
ax.set(xlim=(-3, 3), ylim=(-3, 3))

plt.show()
