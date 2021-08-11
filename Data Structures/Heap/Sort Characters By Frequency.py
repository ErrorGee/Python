from heapq import *
class Solution:
    def frequencySort(self, s: str) -> str:
        string={}
        for element in s:
            string[element]=string.get(element, 0)+1
        minHeap=[]
        for ele, freq in string.items():
            heappush(minHeap, (freq,ele))
        print(minHeap)
        ReturnString=''
        while minHeap:
            j, element=heappop(minHeap)
            while j!=0:
                ReturnString+=element
                j-=1
        return ReturnString[::-1]
                
