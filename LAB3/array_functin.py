
def data_append(array, file):
    for i, line in enumerate(file):
        if i != 0:
            line_ = line.strip().replace(',', '.').split('\t')
            array.append([float(num) for num in line_])

def x_y_fill(array, array_to_fill, index):
    for num in (array[i][index] for i in range(len(array))):
        array_to_fill.append(num)
