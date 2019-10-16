class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i, num in enumerate(nums):
            if (target-num) in ht:
                return [ht[target-num], i]
            ht[num] = i