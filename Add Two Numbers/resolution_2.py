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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = Solution.reverse(*l1)
        l2 = Solution.reverse(*l2)
        return str(l1+l2)[::-1]

print(Solution.addTwoNumbers(Solution, [2,4,3],[5,6,4]))