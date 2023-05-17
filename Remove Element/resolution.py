class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lista = nums
        i = 0

        while i < len(nums):
            if lista[i] == val:
                lista.pop(i)
            else:
                i += 1
        
        return len(lista)


numbers = [0,1,2,2,3,0,4,2]
valor = 2
print(Solution.removeElement(Solution, numbers, valor))