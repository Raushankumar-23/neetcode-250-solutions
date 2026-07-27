class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        n=len(nums)
        hash_map={}
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1

        for k,v in hash_map.items():
            if v>1:
                return True
        return False