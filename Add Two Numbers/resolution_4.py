# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def addTwoNumbers(self, l1, l2):

        def node_to_list(node):
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        def reverse(*args):
            result = ''
            for item in list(reversed(args)):
                result += str(item)
            return int(result)

        def to_list(received):
            result = []
            for number in received:
                result.append(int(number))
            return str(result).replace('[','').replace(']','')

        # def to_list(received):
        #     list_node = ListNode()
        #     for node in received:
        #         if list_node.val:
        #             pointer = list_node.val
        #             while (pointer.next):
        #                 pointer = pointer.next
        #             pointer.next = ListNode(node)
        #         else:
        #             list_node.val = ListNode(node)
        #     return list_node
        

        l1 = reverse(*node_to_list(l1))
        l2 = reverse(*node_to_list(l2))

        return ListNode(str(to_list(str(l1+l2)[::-1])).replace(' ',''))