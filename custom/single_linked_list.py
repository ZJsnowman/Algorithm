from custom.node import Node


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        temp = Node(data)
        if self.is_empty():
            self.head = temp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temp

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def search(self, item):
        current = self.head
        while current is not None:
            if current.item == item:
                return True
            else:
                current = current.next
        return False

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.item == item:
                return count
            else:
                current = current.next
                count += 1
        return -1

    def remove(self, item):
        current = self.head
        pre = None
        while current is not None:
            if current.next == item:
                pre.next = current.next
                break
            else:
                pre = current
                current = current.next

    def size(self):
        current = self.head
        size = 0
        while current is not None:
            size += 1
            current = current.next
        return size

    def insert(self, pos, item):
        node = Node(item)
        if pos < 1:
            self.add(item)
        elif pos >= self.size():
            self.append(item)
        else:
            current = self.head
            for _ in range(pos - 1):
                pre = current
                current = current.next
            pre.next = node
            node.next = current

    def travel(self):
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next

    def reverse(self):
        pre = None
        current = self.head
        while current:
            next_temp = current.next
            current.next = pre
            pre = current
            current = next_temp
        self.head = pre




if __name__ == '__main__':
    a = SingleLinkedList()
    # for i in range(1, 10):
    # a.append(i)
    # print(a.size())
    # a.travel()
    # print(a.search(6))
    # print(a.index(5))
    # a.remove(4)
    # a.travel()
    # a.insert(4, 100)
    # a.travel()
    # print(a.size())
    # a.travel()
    # a.reverse()
    # a.travel()

