class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            return int(str(x)[::-1])
        return int(str(abs(x))[::-1])*-1