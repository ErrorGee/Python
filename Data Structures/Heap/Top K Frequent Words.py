from heapq import *
from collections import deque
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or k<=0:
            return []
        maxHeap=[]
        FrequentWords={}
        for word in words:
            FrequentWords[word]=FrequentWords.get(word, 0)+1
        #print(FrequentWords)
        for word, freq in FrequentWords.items():
            heappush(maxHeap, (-freq, word))
            print(maxHeap)
            # if len(maxHeap)>k:
            #     heappop(maxHeap)
            # print(maxHeap)
        result=[]
        while maxHeap:
            result.append(heappop(maxHeap)[1])
        return result[0:k]
        
        
        
        
