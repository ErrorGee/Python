class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap=[]
        for point in points:
            x=point[0]
            y=point[1]
            distance=(x**2)+(y**2)
            heappush(maxHeap, (-distance, x,y))
            if len(maxHeap)>k:
                heappop(maxHeap)
        # print(maxHeap)
        result=[]
        while maxHeap:
            distance,x,y=heappop(maxHeap)
            result.append([x,y])
        return result
            
                
        
