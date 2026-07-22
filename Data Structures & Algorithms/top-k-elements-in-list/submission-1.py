from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for _ in range(len(nums) + 1)]

        freq = Counter(nums)
        for key, value in freq.items():
            buckets[value].append(key)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if not buckets[i]:
                continue
            
            for item in buckets[i]:
                if k == 0:
                    return res
                
                res.append(item)
                k -= 1
        
        return res


