#Graph
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

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                queue.extend(set(self.graph[vertex]) - visited)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        if start not in visited:
            print(start)
            visited.add(start)
            for neighbor in self.graph[start]:
                self.dfs(neighbor, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
print("BFS starting from vertex 0:")
g.bfs(0)
print("\nDFS starting from vertex 0:")  
g.dfs(0)
