class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in key:
                return [key[difference], i]
            key[nums[i]] = i
        
        return []