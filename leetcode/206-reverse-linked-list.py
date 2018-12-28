from custom.single_linked_list import SingleLinkedList


# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
# self.val = x
# self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversed_node = None
        current = head
        while current:
            next_temp = current.next
            current.next = reversed_node
            reversed_node = current
            current = next_temp
        return reversed_node


if __name__ == '__main__':
    single_linkedlist = SingleLinkedList()
    for i in range(10):
        single_linkedlist.append(i)
    single_linkedlist.travel()
    sol = Solution()
    reverse_node = sol.reverseList(single_linkedlist.head)
    while reverse_node:
        print(reverse_node.item)
        reverse_node=reverse_node.next
