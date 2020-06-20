from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")


def f(x:float, y: float) -> float:
    return np.sin(1/2 * x**2 - 1/4 * y**2 + 3) * np.cos(2*x + 1 - np.e**y)


# x = np.linspace(-np.pi,np.pi,100)
x = np.linspace(-2, 2, 100)
y = x
X, Y = np.meshgrid(x,y)
Z = f(X,Y)

#ax.plot_wireframe(X,Y,Z)
ax.plot_surface(X,Y,Z,cmap="viridis")
plt.show()