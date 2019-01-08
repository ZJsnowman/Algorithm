from custom.node import Node
import heapq


class Queue:
    """
    数组实现队列
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if self.tail == self.capacity:
            if self.head == 0:
                return False
            else:
                for i in range(0, self.tail - self.head):
                    self.items[i] = self.items[i + self.head]
                self.tail = self.tail - self.head
                self.head = 0
        self.items.insert(self.tail, item)
        self.tail += 1
        return True

    def dequeue(self):
        if self.head != self.tail:
            item = self.items[self.head]
            self.head += 1
            return item

    def size(self):
        return len(self.items)

    def __repr__(self):
        return ' '.join(item for item in self.items[self.head:self.tail])


class CycleQueue:
    """
    数组实现循环队列
    """

    def __init__(self, capacity):
        self.items = []
        self.capacity = capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        self.items.insert(self.tail, item)
        self.tail += 1

    def dequeue(self):
        pass

    def __repr__(self):
        pass


class LinkedQueue:
    """
    链表实现队列

    """

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        node = Node(item)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node  # 头指针只用记录第一个结点即可
        self.tail = node

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(current.item)
            current = current.next
        return "->".join(value for value in values)

    def dequeue(self):
        if self.head:
            value = self.head.item
            self.head = self.head.next
            return value

        else:
            return -1

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def travel(self):
        current = self.head
        while current:
            print(current.item)


class PriorityQueue:
    def __init__(self):
        self.items = []
        self.index = 0

    def enqueue(self, item, priority):
        heapq.heappush(self.items, (-priority, self.index, item))

    def dequeue(self):
        return heapq.heappop(self.items)[-1]


if __name__ == '__main__':
    # queue = Queue()
    # queue = LinkedQueue()
    # queue.enqueue('z')
    # queue.enqueue('h')
    # queue.enqueue('a')
    # queue.enqueue('n')
    # queue.enqueue('g')
    # print(queue)
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())
    # # print(queue.size())
    # print('----------')
    # print(queue)

    # q = Queue(12)
    # for i in range(10):
    #     q.enqueue(str(i))
    # print(q)
    #
    # for _ in range(3):
    #     q.dequeue()
    # print(q)
    #
    # q.enqueue("7")
    # q.enqueue("8")
    # print(q)

    q = PriorityQueue()
    q.enqueue('foo', 1)
    q.enqueue('bar', 5)
    q.enqueue('spam', 4)
    q.enqueue('grok', 1)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
