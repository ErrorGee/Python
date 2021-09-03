class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start==0 and end==0:
            return True
        graph=self.makeGraph(n, edges)
        VisitedArr=[False]*(n+1)
        for node in range(1,n+1):
            connect_list=[]
            if VisitedArr[node] ==False:
                self.connectedVertex(node, graph, VisitedArr, connect_list)
                if start in connect_list and end in connect_list:
                    return True
        return False
                
    def makeGraph(self, n, edges):
        dictionary_edge={}
        for i in range(n+1):
            dictionary_edge[i]=list()
        for edge in edges:
            dictionary_edge[edge[0]].append(edge[1])
            dictionary_edge[edge[1]].append(edge[0])
        return dictionary_edge 
    
    def connectedVertex(self, node, graph, VisitedArr, connect_list):
        VisitedArr[node]=True
        connect_list.append(node)
        for neighbour in graph[node]:
            if VisitedArr[neighbour] is not True:
                self.connectedVertex(neighbour, graph, VisitedArr, connect_list)
        return connect_list
                
        
        
        
