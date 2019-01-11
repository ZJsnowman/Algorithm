from custom.node import Node


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        low = fast = head
        while low and low.next:
            low = low.next
            fast = fast.next.next

            if low == fast:
                print(low.item)
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    p1 = Node(1)
    p2 = Node(2)
    p3 = Node(3)
    p4 = Node(4)
    p5 = Node(5)
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p3

    # current = p1
    # while current:
    #     print(current.item)
    #     current = current.next
    print(s.hasCycle(p1))
