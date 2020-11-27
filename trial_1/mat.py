import matplotlib.pyplot as plt
import numpy as np


y_ = []
x_ = []
ut.println();
for i in range(10):
    y_.append(i ** 2)
    x_.append(i ** 2.3)

plt.plot(x_)
plt.plot(y_)
plt.show()