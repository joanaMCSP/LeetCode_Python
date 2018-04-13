class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        repeated = set()
        for num in nums:
            if not num in repeated:
                repeated.add(num)
            else:
                return True
        return False

        
