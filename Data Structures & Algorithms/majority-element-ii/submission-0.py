class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n=len(nums)
        ans=[]
        hash_map={}
        for i in range(n):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1

        for k,v in hash_map.items():
            if v>n/3:
                ans.append(k)

        return ans
        
        