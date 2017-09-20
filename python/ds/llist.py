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
        print("Printing the nodes: ", end='')
        temp = self.head
        while(temp):
            print ("{0} ".format(temp.data), end='')
            temp = temp.next

    # Function to insert a node in the begining
    def push(self, new_data):
        # temp = self.head
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a node at the end.
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            # If the list is empty just set the new node as the new head
            self.head = new_node
        else:
            # Iterate through the list and get the last node
            temp = self.head
            while (temp.next):
                temp = temp.next
            temp.next = new_node

    # Function to insert a node after the given preiv_ndoe
    def insertAfter(self, prev_node, new_data):
        pass


def main():
    # Start with the empty list
    llist = LinkedList()

    # Insert 6.  So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    print ('Created linked list is:')
    llist.printList()


if __name__ == "__main__":
    main()
