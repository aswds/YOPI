def data_append(array, file):
    for i, line in enumerate(file):
        if i != 0:
            array.append(int(line.strip()))
