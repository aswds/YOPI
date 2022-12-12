import numpy as np
import matplotlib.pyplot as plt


def scatter_diagram(x, y):
    plt.scatter(x, y)
    plt.title("Діаграма розсіювання даних \n Тренд позитивний")
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x),  linewidth=2)
    plt.show()
