# This programs represents a greedy coloring Graph algorithm

# Graph class represents the graph object
class buildGraph:

    # Constructor
    def __init__(self, edges, Number):
        self.adjacent = [[] for _ in range(Number)]
 
        # adding edges to the graph
        for (start, target) in edges:
            self.adjacent[start].append(target)
            self.adjacent[target].append(start)
 
# this function will assign the colors to each vertex
def colorGraph(buildGraph):
 
    # Color storage for colors assigned to vertices 
    ColorStorage = {}
 
    # assigning colors to each vertex
    for ver in range(Number):
        #check neighboring colors and assign/store it in ver 
        assigned = set([ColorStorage.get(i) for i in graph.adjacent[ver] if i in ColorStorage])
 
        # check for first available color in the color array
        color = 0
        for c in assigned:
            if color != c:
                break
            color = color + 1
 
        # assign first available color to vertex ver
        ColorStorage[ver] = color
 
    for v in range(Number):
        print("Vertex", v, "color = ", colors[ColorStorage[v]])

# Color graph
if __name__ == '__main__':
    # Array of colors needed for this specific graph
    colors = ["Yellow", "Blue", "Red", "Purple"]
 
    # Number of Vertices
    Number = 6

    #    0------1     2
    #    | \    |\   /|
    #    |   \  | \ / |
    #    |    \ | / \ |
    #    5------4     3
    # array of edges and vertices to represent the graph above
    edges = [(0, 1), 
             (0, 4), 
             (0, 5), 
             (5, 4), 
             (1, 4), 
             (1, 3), 
             (2, 4), 
             (2, 3)]
 
    # populate graph with edge array
    graph = buildGraph(edges, Number)
 
    # run GraphColoring functions
    colorGraph(graph)
