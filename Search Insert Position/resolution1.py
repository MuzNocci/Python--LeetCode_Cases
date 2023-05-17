class Solution(object):
    def searchInsert(self, nums, target):

        lista = []
        if target in nums:
            lista.extend(nums)
        else:
            lista.extend(nums)
            lista.append(target)

        return sorted(lista).index(target)

print(Solution.searchInsert(Solution, [1,3,5,6], 2))