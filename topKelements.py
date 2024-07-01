class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        hashmap={}
        for n in nums:
            if n in hashmap:
                hashmap[n]+=1
                if hashmap.get(n)==k:
                    result.append(n)
            else:
                hashmap[n]=1
                
                
        
        
                    