class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        s = x[::-1]
        if s == x:
            return True
        else:
            return False
