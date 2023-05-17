class Solution(object):
    def lengthOfLongestSubstring(self, s):

        if len(s) == 1:
            return 1

        new_s = ''
        i, count = 0, 0

        while i < len(s):

            if s[i] not in new_s:
                new_s += s[i]
            else:
                new_s = new_s[new_s.index(s[i])+1:] + s[i]

            i += 1

            if len(new_s) > count:
                count = len(new_s)
            
        return count


print(Solution.lengthOfLongestSubstring(Solution,'abcabcbb'))