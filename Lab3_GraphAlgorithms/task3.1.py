"""
Граф G задан списками смежностей вершин. Найти компоненты связности данного графа. 
Определить, является ли граф эйлеровым; если это так - построить эйлеров цикл. 
Определить, двудольный ли граф; если это так - найти разбиение на доли.
"""

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    # функция выполняет глубинный поиск, начиная с текущей вершины, и добавляет все посещенные вершины в текущую компоненту связности
    def dfs(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, component)

    def find_components(self):
        visited = {v: False for v in self.graph} # словарь, где ключи - вершины графа, а значения - булевы флаги, показывающие, была ли данная вершина посещена или нет
        components = []
        for v in self.graph: # глубинный поиск (DFS) для нахождения компонент связности в графе
            if not visited[v]:
                component = []
                self.dfs(v, visited, component)
                components.append(component)
        return components #  список, содержащий все компоненты связности в графе

    def is_eulerian(self):
        for v in self.graph:
            if len(self.graph[v]) % 2 != 0:
                return False
        return True

    def eulerian_cycle(self):
        if not self.is_eulerian():
            return None
        visited_edges = set() # для отслеживания уже посещенных рёбер
        cycle = []

        # функция использует глубинный поиск для прохода по рёбрам графа, добавляя вершины в цикл в обратном порядке
        def dfs_eulerian(v): 
            for neighbor in self.graph[v]:
                edge = (v, neighbor)
                if edge not in visited_edges:
                    visited_edges.add(edge)
                    dfs_eulerian(neighbor)
                    cycle.append(v)

        start_vertex = next(iter(self.graph)) # стартовая вершина для начала эйлерова цикла (первая вершина из графа)
        dfs_eulerian(start_vertex)
        cycle.reverse()
        return cycle

    def is_bipartite(self):
        color = {}

        def dfs_bipartite(v, c):
            color[v] = c
            for neighbor in self.graph[v]:
                if neighbor not in color:
                    if not dfs_bipartite(neighbor, c ^ 1):
                        return False
                elif color[neighbor] == c:
                    return False
            return True

        for v in self.graph:
            if v not in color:
                if not dfs_bipartite(v, 0):
                    return False
        return True

    def bipartition(self):
        if not self.is_bipartite():
            return None
        color = {} #  использование двух цветов (0 и 1)
        for v in self.graph: # глубинный поиск (DFS), чтобы пройтись по всем вершинам графа и покрасить их в один из двух цветов
            color[v] = 0
        for v in self.graph:
            for neighbor in self.graph[v]:
                if color[neighbor] == color[v]: # покрасить вершины так, чтобы соседние вершины имели разные цвета
                    color[neighbor] = 1 - color[v]
        return color # словарь, где ключи - вершины графа, а значения - их цвета

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(4, 5)

    components = g.find_components()
    print("Компоненты связности:", components)

    if g.is_eulerian():
        eulerian_cycle = g.eulerian_cycle()
        print("Эйлеров цикл:", eulerian_cycle)
    else:
        print("Граф не является эйлеровым")

    if g.is_bipartite():
        bipartition = g.bipartition()
        print("Двудольное разбиение:", bipartition)
    else:
        print("Граф не является двудольным")
