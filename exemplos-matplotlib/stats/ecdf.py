import matplotlib.pyplot as plt
import numpy as np

plt.style.use("_mpl-gallery")

np.random.seed(1)
x = 4 + np.random.normal(0, 1.5, 200)

fig, ax = plt.subplots()
ax.ecdf(x)

plt.show()
