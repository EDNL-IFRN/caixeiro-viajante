import csv
from model.graph import Graph
from functions.dfs import find_shortest_path
import networkx as nx
import matplotlib.pyplot as plt
import time

def add_edges(file_path, graph: Graph):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        for row in csv_reader:
            graph.add_edge(row[0].lower(), row[1].lower(), int(row[2]))

def get_vertices(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        vertices = set()
        for row in csv_reader:
            vertices.add(row[0].lower())
            vertices.add(row[1].lower())
    return list(vertices)

def visualize_graph(graph: Graph, path=None):
    G = nx.Graph()
    for v in graph.vertices:
        G.add_node(v)
    for i in range(graph.num_vertices):
        temp = graph.array[i].head
        while temp:
            G.add_edge(graph.vertices[i], temp.value, weight=temp.weight)
            temp = temp.next
    pos = nx.spring_layout(G, k=1.0, iterations=50) 
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600, font_size=6, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    if path:
        for i in range(len(path) - 1):
            nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1])], edge_color='red', width=2)
            plt.pause(1.0)
    
    plt.show()

def main():
    file_path = 'docs/edges.csv'
    vertices = get_vertices(file_path)
    graph = Graph(vertices)
    add_edges(file_path, graph)
    graph.print_graph()
    
    start = input('Digite a cidade inicial: ').lower()
    if start not in vertices:
        print('Cidade inicial inválida')
        print('Cidades disponíveis:', vertices)
        return
    
    end = input('Digite a cidade final: ').lower()
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
        visualize_graph(graph, path)

if __name__ == '__main__':
    main()