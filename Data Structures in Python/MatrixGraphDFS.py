class MatrixGraph:
    """
    :target : 无向图的DFS
    """
    adj_matrix = []
    # function to fill empty adjacency matrix
    def __init__(self, v):
        """
        :param v: number of vertex
        """
        self.v=v
        MatrixGraph.adj_matrix=[[0 for i in range(v)] for j in range(v)]
        self.visited = [False]*v

    # function to add edge to the graph
    def addEdge(self,start,end):
        MatrixGraph.adj_matrix[start][end]=1
        MatrixGraph.adj_matrix[end][start]=1

    # function to perform DFS on the graph
    def DFS(self,start):
        # print current node
        print(start," ")

        # set current node as visited:
        self.visited[start]=True

        # for every node of the graph
        for i in range(self.v):
            # if some node is adjacent to the current node and hasn't been visited yet
            if (MatrixGraph.adj_matrix[start][i]==1) and (not self.visited[i]):
                self.DFS(i)


if __name__ == "__main__":
    v = 5
    g = MatrixGraph(v)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(2,4)

    g.DFS(0)

