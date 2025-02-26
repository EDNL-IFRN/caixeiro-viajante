class Node:
    def __init__(self, value: str, weight: int = None):
        self.value = value
        self.next = None
        self.weight = weight

class List:
    def __init__(self):
        self.head = None

class Graph:
    def __init__(self, vertices: list[str]):
        self.vertices = [v.lower() for v in vertices]
        self.num_vertices = len(vertices)
        self.array = [List() for _ in range(self.num_vertices)]
        self.vertex_index = {v.lower(): i for i, v in enumerate(vertices)}
    
    def add_vertex(self, v: str):
        v = v.lower()
        if v not in self.vertex_index:
            self.vertices.append(v)
            self.vertex_index[v] = self.num_vertices
            new_array = [List() for _ in range(self.num_vertices + 1)]
            for i in range(self.num_vertices):
                new_array[i] = self.array[i]
            
            self.array = new_array
            self.num_vertices += 1
    
    def add_edge(self, v1: str, v2: str, weight: int = None):
        v1 = v1.lower()
        v2 = v2.lower()
        if v1 not in self.vertex_index:
            self.add_vertex(v1)
        if v2 not in self.vertex_index:
            self.add_vertex(v2)
        i1 = self.vertex_index[v1]
        i2 = self.vertex_index[v2]
        new_node = Node(v2, weight)
        new_node.next = self.array[i1].head
        self.array[i1].head = new_node
        new_node = Node(v1, weight)
        new_node.next = self.array[i2].head
        self.array[i2].head = new_node
    
    def print_graph(self):
        for v, i in self.vertex_index.items():
            print(f"Vértice {v}")
            temp = self.array[i].head
            while temp:
                print(f" -> {temp.value}|{temp.weight}|", end="")
                temp = temp.next
            print()