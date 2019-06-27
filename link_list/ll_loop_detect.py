"""
detect a loop in linklist
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
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
        if self.head is None:
            print("empty list")

        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next

    def detect_loop(self):
        temp = self.head

        s = set()
        while temp is not None:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False


if __name__ == "__main__":
    ll = Linklist()
    ll.insert(3)
    ll.insert(5)
    ll.insert(7)
    ll.insert(9)
    ll.head.next.next = ll.head
    # ll.print_list()

    ret = ll.detect_loop()
    if ret is True:
        print("Loop detected")
    else:
        print("Loop not detected")
