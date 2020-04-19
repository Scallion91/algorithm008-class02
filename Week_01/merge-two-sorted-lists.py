# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    array = []

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.recursion(l1)
        self.recursion(l2)
        self.array.sort()
        return self.link(self.array)

    def recursion(self, list: ListNode) -> None:
        if list:
            self.array.append(list.val)
            if list.next:
                self.recursion(list.next)

    def link(self, list) -> ListNode:
        if len(list) == 0:
            return
        else:
            self.head = ListNode(list[0])
            r = self.head
            p = self.head
            for i in list[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
            return r
