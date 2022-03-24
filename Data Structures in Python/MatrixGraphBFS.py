class MatrixGraph:
    """
    :target : 无向图的BFS
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

    # function to perform BFS on the graph
    def BFS(self,start):
        queue = [start]

        # set source as visited
        self.visited[start]=True
        while queue:
            vis = queue[0]

            #print current node
            print(vis, end =' ')
            queue.pop(0)

            # for every adjacent vertex to the current vertex
            # 把最靠近的点都保存进了queue里，然后回到起初，因为都是每层的点存进了queue里，所以按顺序刚好把每层爬完再跑下一层。
            for i in range(self.v):
                if(MatrixGraph.adj_matrix[vis][i]==1) and (not self.visited[i]):
                    # push the adjacent node in the queue
                    queue.append(i)
                    # set
                    self.visited[i]=True




if __name__ == "__main__":
    v = 6
    g = MatrixGraph(v)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,3)
    g.addEdge(2,4)
    g.addEdge(0,5)

    g.BFS(0)