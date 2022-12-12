from array_functin import data_append, x_y_fill
from Diagram import scatter_diagram
from task_2 import task_2
from task_3 import task_3
from task_4 import task_4

file = open('task_03_data/input_100.txt')
answer_file = open('task.txt', 'w')
array = []
x = [1.9,6.2,7.8,10.2,30.9,51.2,18.9,18.0,10.3,11.5]
y = [1.5,8.2,9.4,10.7,24.9,36.9,21.7,19.5,11.0,13.9]
data_append(array=array, file=file)
# x_y_fill(array=array, array_to_fill=x, index=0)
# x_y_fill(array=array, array_to_fill=y, index=1)

scatter_diagram(x, y)
print('Task 2')
task_2(x, y)
print('\n\nTask 3\n')
task_3(y, x,  'Y')
task_3(x, y, 'Y')
print('\n\nTask 4\n')
task_4(x, y, answer_file)
