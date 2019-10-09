class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            # If one of the verts of the edge doesn't exist, can't make that edge
            raise KeyError('Cant create edge, one or more given vertices doesnt exist')

def earliest_ancestor(ancestors, starting_node):
    #Create graph instance
    graph = Graph()

    for pair in ancestors:
        #For each connected vertex, add it to the graph
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        #Then, add edges between the pairs to connect them
        graph.add_edge(pair[1], pair[0])
        
    q = Queue()
    #Enqueue our starting node inside of a list
    q.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        #Grab the most recent path
        path = q.dequeue()
        #Grab the most recent vertice in that path
        v = path[-1]

        #Check to see if our current path is the longest so far, update our max_path_length and set earliest_ancestor
        #To the vertices we've last analyzed
        if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            print(v, earliest_ancestor)
            earliest_ancestor = v
            max_path_length = len(path)
        
        #Add our new paths based on the current vertice we're analyzing
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
            
    #After we've run out of paths, return our earliest ancestor
    return earliest_ancestor