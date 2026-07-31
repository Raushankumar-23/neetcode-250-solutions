class Solution:
    def rob(self, nums: List[int]) -> int:

        n=len(nums)
        prev=nums[0]
        prev1=0
        for index in range(1,n):
            if index>1:
                pick=nums[index]+prev1
            else:
                pick=nums[index]

            not_pick=prev
            cur=max(pick,not_pick)
            prev1=prev
            prev=cur

        return prev



        