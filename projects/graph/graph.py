"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            # If one of the verts of the edge doesn't exist, can't make that edge
            raise KeyError('Cant create edge, one or more given vertices doesnt exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()
        # Enqueue our starting vert
        queue.enqueue(starting_vertex)
        # While we still have verts to work with
        while queue.size() > 0:
            # Dequeue next vert
            vertex = queue.dequeue()
            # Check to see if we've found it yet
            if vertex not in visited:
                # If we haven't, then add it
                visited.add(vertex)
                print(vertex)
                # Enqueue verts connected to that vert, and repeat the process
                for next_vert in self.vertices[vertex]:
                    queue.enqueue(next_vert)
    
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        # Push our starting vert to the stack
        stack.push(starting_vertex)
        # While we still have verts in the stack
        while stack.size() > 0:
            # Pop off vert on top
            vertex = stack.pop()
            # If we haven't analyzed that vert yet
            if vertex not in visited:
                # Add the vert
                visited.add(vertex)
                print(vertex)
                # Iterate through that verts connections
                for next_vert in self.vertices[vertex]:
                    # Push vert to stack, and repeat the process
                    stack.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print(starting_vertex)
        # Add the vert we're starting on upon this runtime of the func
        visited.add(starting_vertex)
        # For all children in our starting vert
        for child_vertex in self.vertices[starting_vertex]:
            # Check to see if child/connected vert is in visited
            if child_vertex not in visited:
                # If it isn't, call func with the child vert as starting_vert and bubble our visited set into next call
                self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        visited = set()
        # Enqueue our starting vertex as a path
        qq.enqueue([starting_vertex])
        # While there are paths to make/check
        while qq.size() > 0:
            # Grab our path
            path = qq.dequeue()
            # Grab last vertex in path
            vertex = path[-1]
            # If our vertex hasn't been found yet
            if vertex not in visited:
                # If that vert is our destination
                if vertex == destination_vertex:
                    # We have found our path list
                    return path
                # Else, add our new vert to visited
                visited.add(vertex)
                # Iterate through verts connected to our new vert
                for next_vert in self.vertices[vertex]:
                    # Make a copy of the current path
                    new_path = list(path)
                    # Add the next vert to the path
                    new_path.append(next_vert)
                    # Enqueue our new possible path
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Same explanation as BFS but with stack now for depth-first
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
