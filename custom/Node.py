class Node:
    def __init__(self, data):
        self._item = data
        self._next = None

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setItem(self, newData):
        self._item = newData

    def setNext(self, newNext):
        self._next = newNext
