import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from random import uniform
import matplotlib.animation as animation

class GradientDescent:

    def __init__(self,f:'function', gradient:'function'=None,limx: int=10, limy:int=10, delta:float=.01,
                 learning_rate:float=.3, steps:int=100, criteria:float=1e-6, number_of_points:int=100,
                 theme:str="Blues"):
        self.f = f
        if gradient is not None:
            self.gradient = gradient
        else:
            self.gradient = self.grad
        self.learning_rate = learning_rate
        self.limx = limx
        self.limy = limy
        self.delta = delta
        self.steps = steps
        self.criteria = criteria
        self.x_aprox_min, self.y_aprox_min = self.generate_points()
        self.number_of_point = number_of_points
        self.theme = theme

        # data for plotting
        x = np.linspace(-self.limx, self.limx, number_of_points)
        y = x
        self.X, self.Y = np.meshgrid(x, y)
        self.Z = self.f(self.X, self.Y)

    def grad(self,x:float, y:float):
        df_dx = (self.f(x+self.delta, y)-self.f(x,y))/self.delta
        df_dy = (self.f(x, y+self.delta)-self.f(x,y))/self.delta
        return [df_dx, df_dy]

    def generate_points(self):
        x = [uniform(self.limx, -self.limx)]
        y = [uniform(self.limy, -self.limy)]

        for _ in range(self.steps):
            grad = self.gradient(x[-1], y[-1])
            update_x = self.learning_rate * grad[0]
            update_y = self.learning_rate * grad[1]
            if max(abs(update_x), abs(update_y)) < self.criteria:
                break
            x.append(x[-1] - update_x)
            y.append(y[-1] - update_y)

        return x,y

    def plot(self):
        # function plot
        fig = plt.figure()
        ax = plt.axes(projection="3d")

        surf = ax.plot_surface(self.X, self.Y, self.Z, cmap=self.theme)

        cset = ax.contourf(self.X, self.Y, self.Z, zdir='z', offset=np.min(self.Z), cmap=self.theme)

        # colorbar
        fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, alpha=0.8)

        plt.axis('off')
        plt.show()

    def update(self,i: float):
        self.ax.plot(self.x_aprox_min[:i], self.y_aprox_min[:i], color="green", linewidth=3.0, alpha=0.8)
        self.plt.title('Punto: {:f}, {:f}'.format(self.x_aprox_min[i],self.y_aprox_min[i]))

    def animation(self):
        self.fig, self.ax = plt.subplots()
        self.plt = plt
        # plt.close()

        cset = self.ax.contourf(self.X, self.Y, self.Z, zdir='z', offset=np.min(self.Z), cmap=self.theme)
        # colorbar
        self.fig.colorbar(cset, ax=self.ax, shrink=0.5, aspect=5, alpha=0.8)

        ani = animation.FuncAnimation(self.fig, self.update,
                                      range(len(self.x_aprox_min)), repeat=False)
        #plt.axis('off')
        plt.show()


def f(x: float, y: float) -> float:
    return x ** 2 + y ** 2

def gradient(x: float, y: float) -> list:
    return [2 * x, 2 * y]

gd = GradientDescent(f,limx=10,limy=10)
# gd.plot()
gd.animation()
