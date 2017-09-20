# Node class
class Node(object):
    # Function to initialize the node object
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

# Linked list class contails a node object


class LinkedList(object):
    def __init__(self):
        self.head = None

    def printList(self):
        print("Printing the nodes:")
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next


def main():
    # Start with empty list
    llist = LinkedList()

    # Create ndoes
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    # n = LinkedList(None)

    # Link the nodes
    llist.head.next = second
    second.next = third

    # Print the list
    llist.printList()


if __name__ == "__main__":
    main()
