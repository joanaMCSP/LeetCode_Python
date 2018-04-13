class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_max = -sys.maxint - 1
        curr_max = -sys.maxint - 1
        curr = 0

        for i in range(n):
            curr = nums[i]
            curr_max = max(curr_max + curr, curr)
            total_max = curr_max if curr_max > total_max else total_max

        return total_max
