"""
create ll insert function and print data function
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        temp = self.head

        if temp is None:
            self.head = Node(data)

        else:
            while temp.next is not None:
                temp = temp.next

            temp.next = Node(data)

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":

    start = LinkList()
    start.insert(2)
    start.insert(4)
    start.insert(6)
    start.insert(7)
    start.insert(9)

    start.print_list()