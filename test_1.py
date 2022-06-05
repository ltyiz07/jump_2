import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
fig.set_tight_layout(True)

print("fig size: {0} DPI, size in inches {1}".format(fig.get_dpi(), fig.get_size_inches()))

x = np.arange(0, 20, 0.1)
ax.scatter(x, x + np.random.normal(0, 3.0, len(x)))
line, = ax.plot(x, x - 5, 'r-', linewidth=2)


def update(i):
    line.set_ydata(x - 5 + i)
    return line, ax


animation = FuncAnimation(fig, update, frames=np.arange(0, 10, 0.1), repeat=True, interval=500)

plt.show()
