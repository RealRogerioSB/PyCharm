import matplotlib.pyplot as plt
import numpy as np

plt.style.use("_mpl-gallery-nogrid")

np.random.seed(1)  # correlated
x = np.random.randn(5000)  # noise
y = 1.2 * x + np.random.randn(5000) / 3

fig, ax = plt.subplots()

ax.hexbin(x, y, gridsize=20)
ax.set(xlim=(-2, 2), ylim=(-3, 3))

plt.show()
