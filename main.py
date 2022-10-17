
from file_writer import writeFile
from Visual import showGraph
datafile = open('./task_01_data/input_10.txt')
data = []
graph = []

for line in datafile:
    graph.append(int(line.strip()))
graph.sort()
showGraph(graph)
writeFile(data,graph)
