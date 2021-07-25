#to make a map/dictionary out of the edges
def mapEdges(Edges):
    dictionary_of_edges={}
    for i in range(1, Vertices+1):
        dictionary_of_edges[i]=list()
    for edge in Edges:
        dictionary_of_edges[edge[0]].append(edge[1])
        dictionary_of_edges[edge[1]].append(edge[0])
    #print(dictionary_of_edges)
    return dictionary_of_edges

#for traversal inside the Graph
def traversalQueue(s,Graph, VisitedArray, dfs_traversal):
    #assuming everyone is connected to atleast someone
    VisitedArray[s]=True
    dfs_traversal.append(s)
    for neighbour in Graph[s]:
        if VisitedArray[neighbour] is not True:
            traversalQueue(neighbour, Graph, VisitedArray, dfs_traversal)

#the first function where everything starts
def dfsTraversal(s, Edges, Vertices):
    Graph=mapEdges(Edges)
    VisitedArray=[False]*(Vertices+1)
    dfs_traversal=[]
    traversalQueue(s, Graph, VisitedArray, dfs_traversal)
    return dfs_traversal

if __name__=="__main__":
    Edges=[[1,2],[1,5],[1,7],[2,8],[2,9],[3,6],[3,9],[4,8],[5,7],[6,8]]
    Vertices=10
    #result is a list
    DfsTraversal=dfsTraversal(1,Edges, Vertices)
    print(DfsTraversal)


    #TestCase1: Edges=[[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [4, 5], [4, 6], [5, 6]]
                #Vertices = 6
                #Result=1,2,4,5,3,6
