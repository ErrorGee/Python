class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapme={}
        res=[]
        for i in strs:
            i=sorted(i)
            i="".join(i)
            mapme[i]=list()
        for i in strs:
            a=sorted(i)
            check="".join(a)
            if check in mapme.keys():
                mapme[check].append(i)
        #print(mapme)
        for i in mapme.values():
            res.append(i)
        return res
        
        
