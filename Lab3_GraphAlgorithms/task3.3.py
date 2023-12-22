"""
Есть N узлов, которые необходимо объединить в сеть. 
Известна стоимость прокладки оптоволоконного кабеля между любой парой узлов. 
Требуется спроектировать связную сеть (между любыми узлами которой можно передать сигнал) минимальной стоимости. 
Задачу реализовать двумя алгоритмами.
"""

# Задача о построении связной сети минимальной стоимости между N узлами

# Алгоритм Прима
def prim(graph):
    start_node = list(graph.keys())[0]
    visited = set([start_node])
    minimum_spanning_tree = []
    edges = [
        (weight, start_node, end_node)
        for end_node, weight in graph[start_node]
    ]
    
    while edges:
        edges.sort()
        weight, start_node, end_node = edges.pop(0)
        
        if end_node not in visited:
            visited.add(end_node)
            minimum_spanning_tree.append((weight, start_node, end_node))
            
            for neighbor, neighbor_weight in graph[end_node]:
                if neighbor not in visited:
                    edges.append((neighbor_weight, end_node, neighbor))
    
    return minimum_spanning_tree

# Алгоритм Краскала
def kruskal(graph):
    minimum_spanning_tree = []
    sets = {node: {node} for node in graph}
    edges = []
    
    for start_node in graph:
        for end_node, weight in graph[start_node]:
            edges.append((weight, start_node, end_node))
    
    edges.sort()
    
    for weight, start_node, end_node in edges:
        start_set = sets[start_node]
        end_set = sets[end_node]
        
        if start_set != end_set:
            minimum_spanning_tree.append((weight, start_node, end_node))
            
            for node in end_set:
                start_set.add(node)
                sets[node] = start_set
            
            end_set.clear()
    
    return minimum_spanning_tree

graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 1), ('D', 2)],
    'C': [('A', 3), ('B', 1), ('D', 6)],
    'D': [('B', 2), ('C', 6)]
}

minimum_spanning_tree_1 = prim(graph)
print("Минимальное остовное дерево (Алгоритм Прима):")
for weight, start_node, end_node in minimum_spanning_tree_1:
    print(f"Ребро ({start_node} - {end_node}), вес: {weight}")

minimum_spanning_tree_2 = kruskal(graph)
print("Минимальное остовное дерево (Алгоритм Краскала):")
for weight, start_node, end_node in minimum_spanning_tree_2:
    print(f"Ребро ({start_node} - {end_node}), вес: {weight}")
