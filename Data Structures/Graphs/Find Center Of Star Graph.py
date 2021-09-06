class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vertices=len(edges)+1
        graph=self.makeGraph(edges,vertices)
        maxCount=0
        for edge in graph.keys():
            maxCount=max(len(graph[edge]), maxCount)
            if maxCount==len(graph[edge]):
                storeKey=edge
        return storeKey
            
        
    def makeGraph(self, edges, vertices):
        dictionary={}
        for i in range(vertices+1):
            dictionary[i]=list()
        for edge in edges:
            dictionary[edge[0]].append(edge[1])
            dictionary[edge[1]].append(edge[0])
        return dictionary


            
