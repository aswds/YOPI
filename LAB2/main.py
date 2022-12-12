from Deviation import standart_dev, middle_dev
from array_funcs import data_append
from Percantile_Quartile import percentile, quartile
from task3 import task3
from task4 import task4
from Diagram import show_diagram

file = open('./task_02_data/input_10.txt')
answer_file = open('task.txt', 'w')
array = []

data_append(array, file)

standart_dev(array, answer_file)
middle_dev(array, answer_file)
percentile(90, len(array), answer_file)
quartile(1, len(array), answer_file)
quartile(3, len(array), answer_file)
task3(array, answer_file)
task4(array, answer_file)
show_diagram(array)
