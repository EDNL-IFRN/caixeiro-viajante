import csv
from model.graph import Graph
from functions.dfs import dfs_path

def add_edges(file_path, graph: Graph):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        for row in csv_reader:
            graph.add_edge(row[0], row[1], int(row[2]))

def get_vertices(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        vertices = set()
        for row in csv_reader:
            vertices.add(row[0])
            vertices.add(row[1])
    return list(vertices)

def main ():
    file_path = 'docs/edges.csv'
    vertices = get_vertices(file_path)
    graph = Graph(vertices)
    add_edges(file_path, graph)
    graph.print_graph()
    start = input('Enter the start vertex: ')
    end = input('Enter the end vertex: ')
    if(start not in vertices or end not in vertices):
        print('Invalid vertices')
        print('Vertices: ', vertices)
        return
    path, cost = dfs_path(graph, start, end)
    print('Path: ', path)   
    print('Cost: ', cost)
main()