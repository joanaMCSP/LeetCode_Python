class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = sys.maxint
        maxDiff = 0

        for price in prices:
            if price < min:
                min = price
            elif price - min > maxDiff:
                maxDiff = price - min
        return maxDiff
