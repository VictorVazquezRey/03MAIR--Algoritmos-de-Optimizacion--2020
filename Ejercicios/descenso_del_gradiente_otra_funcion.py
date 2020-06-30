import numpy as np
import matplotlib.pyplot as plt
from random import uniform
import matplotlib.animation as animation



fig, ax = plt.subplots()

#función
def f(x:float, y: float) -> float:
    return np.sin(1/2 * x**2 - 1/4 * y**2 + 3) * np.cos(2*x + 1 - np.e**y)

def gradient(x:float, y:float) -> list:
    return np.gradient(np.array([x,y]))

x = np.linspace(-2, 2, 100)
y = x
X, Y = np.meshgrid(x,y)
Z = f(X, Y)

mycmap = "Blues"

# surf = ax.plot_surface(X, Y, Z, cmap=mycmap,
#                        edgecolor="none", rstride=1, cstride=1,
#                        zorder=0.1, alpha=1)

cset = ax.contourf(X, Y, Z, zdir='z', offset=np.min(Z), cmap=mycmap)

fig.colorbar(cset, ax=ax, shrink=0.5, aspect=5)

# constants
LR = .2
STEPS = 100
CRITERIA = 1e-6


# generation points
x = [uniform(2, -2)]
y = [uniform(2, -2)]

for _ in range(STEPS):
    grad = gradient(x[-1], y[-1])
    if max(abs(LR * grad[0]), abs(LR * grad[1])) < CRITERIA:
        break
    x.append(x[-1] - LR * grad[0])
    y.append(y[-1] - LR * grad[1])

# animation
def update(i: float):
    ax.plot(x[:i], y[:i], color="green", linewidth=3.0, alpha=0.8)


anim = animation.FuncAnimation(fig, update,
                               range(len(x)), repeat=False)
plt.axis('off')
plt.show()