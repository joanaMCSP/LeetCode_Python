import math

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        divisors = [div for div in range(1,int(math.ceil(math.sqrt(num)))) if num % div == 0]
        divisors.extend([num // div for div in divisors if num // div < num])

        return sum(divisors) == num
