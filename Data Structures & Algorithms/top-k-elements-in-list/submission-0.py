class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans=[]
        hash_map={}
        for num in nums:
            hash_map[num]=hash_map.get(num,0)+1

        sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1],reverse=True))

        count=0
        for key in sorted_dict.keys():
            count += 1
            ans.append(key)
            if count==k:
                break
        
        return ans

    


        