"""
find the length of lind list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LindList:
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
        return

    def print_list(self):

        if self.head is None:
            print("enmty list")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next

    def get_length(self):

        if self.head is None:
            print("empty list : 0")

        else:
            count = 0
            temp = self.head
            while temp is not None:
                count += 1
                temp = temp.next

            return count


if __name__ == "__main__":
    head = LindList()
    head.insert(3)
    head.insert(4)
    head.insert(5)
    head.insert(15)
    head.insert(6)
    head.insert(7)

    head.print_list()
    print("count : "+str(head.get_length()))
