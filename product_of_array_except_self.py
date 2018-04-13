class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        output = [0] * n

        for i, num in reversed(list(enumerate(nums))):
            if i < n-1 :
                output[i] = nums[i] * output[i+1]
            else :
                output[i] = nums[i]

        before = 1
        m = len(output)
        for j in range(m-1):
            output[j] = before * output[j+1]
            before *= nums[j]
        output[m-1] = before
        return output
