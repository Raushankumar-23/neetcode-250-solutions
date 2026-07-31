class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n=len(nums)
        total=0
        maxi=float("-inf")
        for num in nums:
            total += num
            maxi=max(maxi,total)
            if total < 0:
                total=0

        return maxi
        