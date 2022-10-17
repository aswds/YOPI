from Numbers import replaceStr, Numbers
import math

task = open('task.txt', 'w')
task.writelines(
    '{0:>5} \t\t||\t\t {1:>5} \t\t||\t\t {2:>5} \t\t||\t\t {3:>5} \n\n'.format('item', 'fi(frequency)', 'Rf',
                                                                               'Fi(cumulative freq.)'))


def printf(data):
    task.writelines(data)


def dispersion(array):
    arr = []
    for item in array:
        arr.append(item)
    n = len(arr)
    mid = sum(map(int, arr)) / n
    print(mid)
    deviations = [(float(x) - mid) ** 2 for x in arr]
    variance = sum(deviations) / n
    return round(variance, 3)


def relative_freq(num, Sum):
    return str(num / Sum)


c = 0


def cumulative_freq(item):
    global c
    c += item
    return str(c)


def count_data_appear(data, graph):
    for i, num in enumerate(graph):
        num_of_number = graph.count(num)
        if graph[i] != graph[i - 1]:
            data.append(Numbers(num, num_of_number))


def write_data(data, arr):
    Sum = sum(map(int, arr))
    for i in range(len(data)):
        print(i)
        line = data[i].__str__()
        printf(
            f'{str(line)}\t\t || \t\t{relative_freq(data[i].number, Sum):>5}\t\t || \t\t {cumulative_freq(data[i].number):>5}')


def writeFile(data, graph):
    print(graph)
    count_data_appear(data, graph)
    write_data(data, graph)
    disputer = dispersion(graph)
    mid_sqr = math.sqrt(disputer)
    Mediana = graph[math.floor((len(graph) / 2))]
    printf(f'\n\n\nMedian:{Mediana}')
    printf(f"\nMid square:{mid_sqr}")
    printf(f'\nModa: {max((num.count, num.number) for num in data)}')
    printf(f'\nVariance: {disputer}')
