class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}

        for i, num in enumerate(nums):

            if target - num in index:
                return [index[target - num],i]
            
            index[num] = i
        
        return []