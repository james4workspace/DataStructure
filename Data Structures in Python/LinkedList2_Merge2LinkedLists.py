# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        head = ptr = ListNode()  # we need head as the first node to declare the position
        # ptr is the node for recursion

        while list1 is not None and list2 is not None:
            val = 0
            if list1.val > list2.val:
                val = list2.val
                list2 = list2.next
            else:
                val = list1.val
                list1 = list1.next
            node = ListNode(val)
            ptr.next = node
            ptr = ptr.next

        # if one line is over, it means the other line can be added directly
        if list1 is not None:
            ptr.next = list1
        elif list2 is not None:
            ptr.next = list2
        return head.next
        # coz we didn't store anything in the head node, so we take the next one as real head