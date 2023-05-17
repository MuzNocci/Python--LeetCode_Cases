class Solution(object):
    def searchInsert(self, nums, target):

        lista = []
        if target in nums:
            lista.extend(nums)
        else:
            lista.extend(nums)
            lista.append(target)

        counter = 0
        answer = 0

        for n in sorted(lista):
            if n == target:
                return counter
            counter += 1

print(Solution.searchInsert(Solution, [1,3,5,6], 2))