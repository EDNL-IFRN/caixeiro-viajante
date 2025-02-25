import csv
from model.graph import Graph
from functions.dfs import find_shortest_path

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

def main():
    file_path = 'docs/edges.csv'
    vertices = get_vertices(file_path)
    graph = Graph(vertices)
    add_edges(file_path, graph)
    graph.print_graph()
    
    start = input('Digite a cidade inicial: ')
    if start not in vertices:
        print('Cidade inicial inválida')
        print('Cidades disponíveis:', vertices)
        return
    
    end = input('Digite a cidade final: ')
    if end not in vertices:
        print('Cidade final inválida')
        print('Cidades disponíveis:', vertices)
        return
    
    path, cost = find_shortest_path(graph, start, end)
    if not path:
        print('Não foi possível encontrar um caminho entre as cidades')
    else:
        print('Menor caminho encontrado:', ' -> '.join(path))
        print('Custo total:', cost)

if __name__ == '__main__':
    main()