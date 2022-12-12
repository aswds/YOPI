def percentile(k, array_len, file):
    Pk = float(k / 100) * (array_len + 1)
    file.write(f'\n{k} Percentile: {Pk}')
    return Pk


def quartile(i, array_len, file):
    Qk = float(i / 4) * (array_len + 1)
    file.write(f'\n{i} Quartile: {Qk}')
    return Qk
