from usable_funcs import avg
import numpy as np


def task_3(x , y , x_or_y = ''):
    x = np.array(x)
    y = np.array(y)
    avg_x = float(avg(x))
    avg_y = float(avg(y))
    # Sxy = sum XY - (sumX)(sumY)/n
    Sxy = np.sum(x * y) - avg_x * avg_y
    #Sxx = sum X^2 - (sumX)^2/n
    Sxx = np.sum(x * x) - avg_x * avg_x
    b = Sxy / Sxx
    a = avg_y - b * avg_x
    print( f"{x_or_y}: {a} + {b}x")
