import node as n


class LinkedList:
    # initialize head
    def __init__(self):
        self.head = None

    # add a new node at the beginning
    def append(self, new_data):
        new_node = n.Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    # print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next