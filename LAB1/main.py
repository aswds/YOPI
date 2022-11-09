
from LAB1.file_writer import writeFile
from LAB1.Visual import showGraph
datafile = open('task_01_data/input_100.txt')
data = []
graph = []

for line in datafile:
    graph.append(int(line.strip()))
graph.sort()
writeFile(data,graph)
showGraph(graph)
