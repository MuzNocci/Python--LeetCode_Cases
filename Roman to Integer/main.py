class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0

        for u in s:

            if u == 'M':
                r = r + 1000
            elif u == 'D':
                r = r + 500
            elif u == 'C':
                r = r + 100
            elif u == 'L':
                r = r + 50
            elif u == 'X':
                r = r + 10
            elif u == 'V':
                r = r + 5
            elif u == 'I':
                r = r + 1
            
        if 'CM' in s:
            r = r - 200
        if 'CD' in s:
            r = r - 200
        if 'XC' in s:
            r = r - 20
        if 'XL' in s:
            r = r - 20
        if 'IX' in s:
            r = r - 2
        if 'IV' in s:
            r = r - 2

        return r