"""
find the length of lind list
"""


class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LindList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        temp = self.head

        if self.head is None:
            self.head = Node(data)

        else:

if __name__ == "__main__":
    head = LindList()
