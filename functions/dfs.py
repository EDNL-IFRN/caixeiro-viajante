from model.graph import Graph

def _dfs(graph: Graph, current: str, end: str, visited: set, path: list, 
         current_cost: int, best_data: dict):
    if current == end:
        if current_cost < best_data['min_cost']:
            best_data['min_cost'] = current_cost
            best_data['best_path'] = path.copy()
        return
    
    visited.add(current)
    path.append(current)
    
    current_index = graph.vertex_index[current]
    temp = graph.array[current_index].head
    while temp:
        if temp.value not in visited:
            _dfs(graph, temp.value, end, visited, path, 
                 current_cost + temp.weight, best_data)
        temp = temp.next
    
    path.pop()
    visited.remove(current)

def find_shortest_path(graph: Graph, start: str, end: str):
    visited = set()
    best_data = {
        'best_path': [],
        'min_cost': float('inf')
    }
    
    _dfs(graph, start, end, visited, [], 0, best_data)
    
    return (best_data['best_path'] + [end] if best_data['best_path'] else [], 
            best_data['min_cost'] if best_data['min_cost'] != float('inf') else 0)