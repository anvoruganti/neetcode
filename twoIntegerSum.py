class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        result=[]
        for i in range(len(nums)):
            k=target-nums[i]
            if k in hashset:
                k_index=hashset.get(k)
                result.append(k_index)
                result.append(i)
            hashset[nums[i]]=i
        return result


        
        