class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        seen = {}
        for i in range(length):
            if (seen.get(nums[i]) is not None):
                return [seen.get(nums[i]), i]
            seen[target - nums[i]] = i
        return None
