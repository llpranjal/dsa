from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq = Counter(nums)
        total = 0
        #for each color
        for i in range(3):
            #while there are still more of the color
            while freq[i]:
                nums[total] = i
                freq[i] -= 1
                total += 1
        
        return nums


