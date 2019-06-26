"""
find nth node of ll from last
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = Node(data)

    def print_list(self):
        if self.head is None:
            print("empth list")

        else:
            temp = self.head

            while temp is not None:
                print(temp.data)
                temp = temp.next

    def nth_node_from_last(self, index):

        if self.head is None:
            print("empty list")
            return

        else:
            count = 0
            temp = self.head
            while temp.next is not None:
                count += 1
                temp = temp.next

            if count < index:
                return "index out of bound"

            index_from_start = count - index + 1

            temp = self.head

            for p in range(index_from_start):
                temp = temp.next

            return temp.data


if __name__ == "__main__":
    head = Linklist()
    head.insert(3)
    head.insert(4)
    head.insert(6)
    head.insert(7)
    head.insert(9)
    head.print_list()
    print("----------------nth element from last------------------")
    print(head.nth_node_from_last(51))
