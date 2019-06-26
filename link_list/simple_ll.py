"""
create 3 nodes link list and print data
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LindList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    start = LindList()

    start.head = Node(1)
    second = Node(2)
    third = Node(3)

    start.head.next = second
    second.next = third

    start.print_list()

