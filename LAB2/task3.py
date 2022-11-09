import numpy as np
from Deviation import avg
from Deviation import writeFile


def task3(array, file):
    avg_n = avg(array)
    res_array = []
    array_len = len(array)
    A = np.array([[100, 1], [avg_n, 1]])
    X = np.linalg.solve(A, np.array([100, 95]))

    for i in range(array_len):
        res_array.append((X[0] * array[i] + X[1]))

    writeFile(file, f"\nA = {X[0]}\nB = {X[1]}")
    writeFile(file, f"\nMarks:{res_array}")
