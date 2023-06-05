class Graph:
    def __init__(self):
        self._data = {}

    def addVertex(self, key):
        if key not in self._data:
            self._data[key] = set()

    def addEdge(self, start, end):
        self._data[start].add(end)

    def vertex(self):
        print("Seluruh Node =", " ".join(self._data.keys()))

    def edge(self):
        edges = []
        for start, ends in self._data.items():
            for end in ends:
                edges.append(f"{start}{end}")
        print("Seluruh Edge =", " ".join(edges))

    def bfs(self, node):
        visited = set()
        queue = [node]
        visited.add(node)
        while queue:
            current_node = queue.pop(0)
            print(current_node, end=" ")
            for neighbor in self._data[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print("\n")


graph = Graph()

graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('d', 'e')
graph.addEdge('c', 'g')
graph.addEdge('c', 'e')
graph.addEdge('e', 'f')

graph.vertex()
graph.edge()
graph.bfs("a")
