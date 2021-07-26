#make graph of all the edges
def mapEdges(Edges):
    dictionary_of_edges={}
    for i in range(Vertices+1):
        dictionary_of_edges[i]=list()
    for edge in Edges:
        dictionary_of_edges[edge[0]].append(edge[1])
        dictionary_of_edges[edge[1]].append(edge[0])
    return dictionary_of_edges

#count connectedcomponents in one group
def countConnected(node, Graph, VisitedArray):
    Count=1
    VisitedArray[node]=True
    for neighbour  in Graph[node]:
        if VisitedArray[neighbour] is not True:
            Count+=countConnected(neighbour, Graph, VisitedArray)
    return Count

#the start of everything
def dfsTraversal(s, Edges, Vertices):
    Graph=mapEdges(Edges) 
    VisitedArray=[False]*(Vertices+1)
    store_count=[]
    for node in range(1, Vertices+1):
        if VisitedArray[node]==False:
            CountVals=countConnected(node, Graph, VisitedArray)
            store_count.append(CountVals)
    return store_count
        
if __name__=="__main__":
    Edges=[[1,5],[1,7],[2,4],[2,8],[3,9],[3,6],[10,11],[11,12],[12,14],[13,14]]
    Vertices=14
    count_list=dfsTraversal(1,Edges, Vertices)
    print(count_list)
