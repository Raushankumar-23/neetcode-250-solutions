class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = []

        # Prefix products
        prefix = [1] * n
        p = 1
        for i in range(n):
            prefix[i] = p
            p *= nums[i]

        # Suffix products
        suffix = [1] * n
        p = 1
        for i in range(n - 1, -1, -1):
            suffix[i] = p
            p *= nums[i]

        # Final answer
        for i in range(n):
            ans.append(prefix[i] * suffix[i])

        return ans