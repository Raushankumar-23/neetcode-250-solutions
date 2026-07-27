class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        list=[]
        for i in range(n):
            for j in range(n):
                nums[i]+nums[j] == target
                list.apend(i,j)
        
        