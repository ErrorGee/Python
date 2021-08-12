from heapq import *
class Solution:
    def reorganizeString(self, s: str) -> str:
        HashMap={}
        for string in s:
            HashMap[string]=HashMap.get(string, 0)+1
        MaxHeap=[]
        for string, freq in HashMap.items():
            heappush(MaxHeap, (-freq, string))
        result=""
        # print(MaxHeap)
        PrevElement, PrevFreq=None, None
        while MaxHeap:
            CurrFreq,CurrElement=heappop(MaxHeap)
            CurrFreq=-CurrFreq
            result+=CurrElement
            if PrevElement!=None and PrevFreq>0:
                heappush(MaxHeap, (-PrevFreq, PrevElement))
            PrevElement=CurrElement
            PrevFreq=CurrFreq-1
        if len(result)==len(s):
            return result
        else:
            return ""
        
