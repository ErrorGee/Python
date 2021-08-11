from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dictionary with frequency as value and numebrs as keys
        Elements={}
        for num in nums:
            Elements[num]=Elements.get(num, 0)+1
        #create a heap
        minHeap=[]
        for num, freq in Elements.items():
            heappush(minHeap, (freq,num))
            if len(minHeap)>k:
                heappop(minHeap)
        result=[]
        for i in range(k):
            result.append(heappop(minHeap)[1])
        return result
        
        
        
