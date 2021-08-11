from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while (len(stones)>=0):
            if len(stones)==0:
                return 0
            elif (len(stones)==1):
                return stones[0]
            minHeap=[]
            for i in range(2):
                heappush(minHeap, stones[i])
            for i in range(2,len(stones)):
                if stones[i]>minHeap[0]:
                    heappop(minHeap)
                    heappush(minHeap,stones[i])
            stones.remove(minHeap[0])
            stones.remove(minHeap[1])
            if minHeap[0]==minHeap[1]:
                pass
            else:
                stones.append(abs(minHeap[0]-minHeap[1]))
