from custom.single_linked_list import SingleLinkedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverse(self, head):
        reverse_head = None
        current = head
        while current:
            next_temp = current.next
            current.next = reverse_head
            reverse_head = current
            current = next_temp

        return reverse_head

    def isPalindrome(self, head):
        if head is None:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reversed_node = self.reverse(slow)
        current = head
        while current and reversed_node:
            if current.item != reversed_node.item:
                return False
            current = current.next
            reversed_node = reversed_node.next
        return True


if __name__ == '__main__':
    # the result should be False, True, True, True, True
    test_str_arr = ['ab', 'aa', 'aba', 'abba', 'abcba', [0,0]]
    sol = Solution()
    for str in test_str_arr:
        l = SingleLinkedList()
        for i in str:
            l.append(i)
        print(sol.isPalindrome(l.head))
