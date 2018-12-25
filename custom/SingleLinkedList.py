from custom.Node import Node


class SingleLinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def append(self, data):
        temp = Node(data)
        if self.is_empty():
            self._head = temp
        else:
            current = self._head
            while (current.getNext() != None):
                current = current.getNext()
            current.setNext(temp)

    def add(self, data):
        temp = Node(data)
        temp.setNext(self._head)
        self._head = temp

    def search(self, item):
        current = self._head
        while current is not None:
            if current.getItem() == item:
                return True
            else:
                current = current.getNext()
        return False

    def index(self, item):
        current = self._head
        count = 0
        while (current is not None):
            if current.getItem() == item:
                return count
            else:
                current = current.getNext()
                count += 1
        return -1

    def remove(self, item):
        current = self._head
        pre = None
        while current is not None:
            if current.getItem() == item:
                pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    def size(self):
        current = self._head
        size = 0
        while current is not None:
            size += 1
            current = current.getNext()
        return size

    def insert(self, pos, item):
        node=Node(item)
        if pos < 1:
            self.add(item)
        elif pos >= self.size():
            self.append(item)
        else:
            current = self._head
            for _ in range(pos-1):
                pre = current
                current = current.getNext()
            pre.setNext(node)
            node.setNext(current)

    def travel(self):
        current = self._head
        while current is not None:
            print(current.getItem())
            current = current.getNext()


if __name__ == '__main__':
    a = SingleLinkedList()
    for i in range(1, 10):
        a.append(i)
    # print(a.size())
    # a.travel()
    # print(a.search(6))
    # print(a.index(5))
    # a.remove(4)
    # a.travel()
    a.insert(4, 100)
    a.travel()
    print(a.size())
