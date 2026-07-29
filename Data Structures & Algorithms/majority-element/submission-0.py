class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hash_map={}
        n=len(nums)
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1

        for k,v in hash_map.items():
            if v>n/2:
                return k
        