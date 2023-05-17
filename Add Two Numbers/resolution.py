# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def reverse(*args):
        result = ''
        for item in list(reversed(args)):
            result += str(item)
        return int(result)
    
    def into_list(self, received):
        result = []
        for number in received:
            result.append(int(number))
        return result

    def addTwoNumbers(self, l1, l2):
        l1 = Solution.reverse(*l1)
        l2 = Solution.reverse(*l2)
        return Solution.into_list(object, str(l1+l2)[::-1])


print(Solution.addTwoNumbers(object, [9,9,9,9,9,9,9], [9,9,9,9]))