from model.graph import Graph

def dfs_path(graph: Graph, start: str, end: str):
        visited = set()
        best_path = []
        min_cost = float('inf')  # Inicializa com infinito para garantir encontrar o menor
    
        def dfs_recursive(current: str, path: list, current_cost: int):
            nonlocal best_path, min_cost
            visited.add(current)
            path.append(current)
            
            if current == end and current_cost < min_cost:
                min_cost = current_cost
                best_path = path.copy()
            
            current_index = graph.vertex_index[current]
            temp = graph.array[current_index].head
            while temp:
                if temp.value not in visited:
                    dfs_recursive(temp.value, path, current_cost + temp.weight)
                temp = temp.next
            
            path.pop()
            visited.remove(current)
        
        dfs_recursive(start, [], 0)
        return best_path, min_cost if min_cost != float('inf') else 0