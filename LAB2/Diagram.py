import matplotlib.pyplot as plt


def show_diagram(array):
    plt.grid()
    plt.boxplot(array)
    plt.show()
