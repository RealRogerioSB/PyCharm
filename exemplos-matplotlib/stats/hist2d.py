import matplotlib.pyplot as plt
import numpy as np

plt.style.use("_mpl-gallery-nogrid")

np.random.seed(1)  # correlated
x = np.random.randn(5000)  # noise
y = 1.2 * x + np.random.randn(5000) / 3

fig, ax = plt.subplots()

ax.hist2d(x, y, bins=(np.arange(-3, 3, 0.1), np.arange(-3, 3, 0.1)))
ax.set(xlim=(-2, 2), ylim=(-3, 3))

plt.show()
