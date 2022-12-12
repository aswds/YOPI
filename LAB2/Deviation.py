import math


def writeFile(file, data):
    file.write(str(data))


def avg(array):
    sum = 0
    for num in array:
        sum += num
    return sum / len(array)


def variance(array):
    avg_n = avg(array)
    frequency_sum = 0
    sum_ = 0
    for num in array:
        sum_ += array.count(num) * (num - avg_n) ** 2
        frequency_sum += array.count(num)
    return sum_ / frequency_sum


def standart_dev(array, file):
    var_x = variance(array)
    writeFile(file, f"Standard Deviation:{math.sqrt(var_x)}\n")
    return math.sqrt(var_x)


def middle_dev(array, file):
    sum_ = 0
    avg_n = avg(array)
    array_len = len(array)
    for i in range(array_len - 1):
        sum_ += math.fabs(array[i] - avg_n)
    res = sum_ / array_len
    writeFile(file, f"Middle Deviation:{res}")
