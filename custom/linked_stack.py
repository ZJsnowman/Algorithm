from custom.node import Node


class LinkedStack:
    """
    基于链表实现栈
    """
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return -1
        value = self.head.item
        self.head = self.head.next
        return value


if __name__ == '__main__':
    l = LinkedStack()
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    l.push(5)
    l.push(6)
    print(l.pop())
    print(l.pop())
    print(l.pop())
    print(l.pop())
    print(l.pop())
    print(l.pop())
    print(l.pop())
