"""
delete given key
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

    def print(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            temp = self.head

            while temp is not None:
                print(temp.data)
                temp = temp.next

    def delete(self, data):
        if self.head is None:
            print("List is empty")
            return

        else:
            temp1 = self.head
            temp2 = self.head.next

            while temp2 is not None:
                if temp2.data != data:
                    temp1 = temp2
                    temp2 = temp2.next

                else:
                    temp1.next = temp2.next
                    print("data deleted : {}".format(data))
                    return
            else:
                print("data not found")


if __name__ == "__main__":
    start = LinkList()
    start.insert(3)
    start.insert(5)
    start.insert(7)
    start.insert(8)
    start.insert(9)

    start.print()

    start.delete(7)

    start.print()


