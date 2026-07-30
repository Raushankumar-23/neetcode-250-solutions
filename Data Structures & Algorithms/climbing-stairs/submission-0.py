class Solution:
    def climbStairs(self, n: int) -> int:

        prev=1
        prev1=1
        for i in range(2,n+1):
            cur=prev+prev1
            prev1=prev
            prev=cur

        return prev
        