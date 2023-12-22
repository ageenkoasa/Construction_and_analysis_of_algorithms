"""
В городе есть N перекрестков и M дорог (каждая дорога начинается и заканчивается перекрестком, дороги имеют направление). 
Известно время проезда каждой дороги (движение двустороннее, и время на движение в одну сторону может не совпадать со временем движения назад). 
Определить перекресток для расположения на нем пожарной станции с условием: пожарная машина должна попасть в наиболее удаленный от станции перекресток за минимальное время (пожарная машина может нарушать ПДД и ехать по встречному направлению). 
Задачу реализовать двумя алгоритмами.
"""

# Задача о поиске наиболее удаленного перекрестка для расположения пожарной станции

# Алгоритм 1: Алгоритм Дейкстры
def dijkstra(graph, start):
    """
    Алгоритм Дейкстры позволяет найти кратчайшие пути от заданной вершины до всех остальных вершин в графе
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()
    
    while True:
        current_distance = float('inf')
        current_vertex = None
        
        for vertex in graph:
            if distances[vertex] < current_distance and vertex not in visited:
                current_distance = distances[vertex]
                current_vertex = vertex
        
        if current_vertex is None:
            break
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex]:
            distance = max(distances[current_vertex], weight)
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances

def find_fire_station_location_1(graph):
    max_distance = float('-inf')
    fire_station_location = None
    
    for vertex in graph:
        distances = dijkstra(graph, vertex)
        min_distance = min(distances.values())
        
        if min_distance > max_distance:
            max_distance = min_distance
            fire_station_location = vertex
    
    return fire_station_location

# Алгоритм 2: Алгоритм Флойда-Уоршелла
def floyd_warshall(graph):
    """
    Алгоритм Флойда-Уоршелла позволяет найти кратчайшие пути между всеми парами вершин взвешенного ориентированного графа
    """
    distances = {vertex: {v: float('inf') for v in graph} for vertex in graph}
    
    for vertex in graph:
        distances[vertex][vertex] = 0
    
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            distances[vertex][neighbor] = weight
    
    for middle_vertex in graph:
        for start_vertex in graph:
            for end_vertex in graph:
                distances[start_vertex][end_vertex] = min(
                    distances[start_vertex][end_vertex],
                    distances[start_vertex][middle_vertex] + distances[middle_vertex][end_vertex]
                )
    
    return distances

def find_fire_station_location_2(graph):
    max_distance = float('-inf')
    fire_station_location = None
    
    distances = floyd_warshall(graph)
    
    for vertex in graph:
        min_distance = max(distances[vertex].values())
        
        if min_distance > max_distance:
            max_distance = min_distance
            fire_station_location = vertex
    
    return fire_station_location

graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 6)],
    'D': []
}

fire_station_1 = find_fire_station_location_1(graph)
print("Перекресток для пожарной станции (Алгоритм Дейкстры):", fire_station_1)

fire_station_2 = find_fire_station_location_2(graph)
print("Перекресток для пожарной станции (Алгоритм Флойда-Уоршелла):", fire_station_2)