import numpy as np
import matplotlib.pyplot as plt
from random import uniform
import matplotlib.animation as animation


# paraboloid function
def f(x: float, y: float) -> float:
    return x ** 2 + y ** 2


def gradient(x: float, y: float) -> list:
    return [2 * x, 2 * y]


# data
x = np.linspace(-10, 10, 100)
y = x
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# theme
mycmap = "Blues"

# function plot
fig = plt.figure()
ax = plt.axes()

cset = ax.contourf(X, Y, Z, zdir='z', offset=np.min(Z), cmap=mycmap)
# colorbar
fig.colorbar(cset, ax=ax, shrink=0.5, aspect=5, alpha=0.8)

# constants
LR = .3
STEPS = 100
CRITERIA = 1e-6


# generation points
x = [uniform(5, -5)]
y = [uniform(5, -5)]

for _ in range(STEPS):
    grad = gradient(x[-1], y[-1])
    if max(abs(LR * grad[0]), abs(LR * grad[1])) < CRITERIA:
        break
    x.append(x[-1] - LR * grad[0])
    y.append(y[-1] - LR * grad[1])



# animation
def update(i: float):
    ax.plot(x[:i], y[:i], color="green", linewidth=3.0, alpha=0.8)
    plt.title(str(x[i]) + ", " + str(y[i]))


ani = animation.FuncAnimation(fig, update,
                              range(len(x)), repeat=False)

plt.axis('off')
plt.show()
