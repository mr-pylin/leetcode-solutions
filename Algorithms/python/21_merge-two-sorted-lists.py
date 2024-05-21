# https://leetcode.com/problems/merge-two-sorted-lists
# difficulty: easy

from typing import Optional

# definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if there is no linked lists, return None
        if not(list1 or list2):
            return None
        
        current = sorted_list = ListNode()

        while list1 or list2:

            if list1 and list2:  # if both of the lists have values
                if list1.val < list2.val:
                    minimum = list1.val
                    list1 = list1.next
                else:
                    minimum = list2.val
                    list2 = list2.next

                current.val = minimum
                current.next = ListNode()
                current = current.next

            elif list1:  # if only list1 has values
                current.val = list1.val
                current.next = list1.next
                break

            elif list2:  # if only list2 has values
                current.val = list2.val
                current.next = list2.next
                break

        return sorted_list


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    sorted_list = Solution().mergeTwoLists(list1, list2)

    while sorted_list:
        print(sorted_list.val)
        sorted_list = sorted_list.next