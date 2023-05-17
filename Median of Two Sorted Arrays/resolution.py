class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):

        varmed = 0
        numbers = sorted(nums1 + nums2)
        mednumbers = len(numbers) / 2
        restnumbers = len(numbers) % 2
        if restnumbers == 0:
            varmed = float((numbers[int(mednumbers)] + numbers[int(mednumbers)-1])) / 2
        else:
            varmed = float(numbers[int(mednumbers)])
        
        return varmed