class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

    def get_data(self):
        return self.data

class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = Node(val)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        return new_node

    def append(self, val):
        new_node = Node(val)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return new_node

    def remove_from_last(self):
        if self.tail is None:
            raise KeyError('ther is no entry to remove.')

        ret_key = self.tail.data
        print ("dlist", ret_key)

        # dlist has only one entry
        if self.tail.prev is None:
            self.tail = None
            self.head = None 
            return ret_key
        
        # dlist has more than one entry.
        prev = self.tail.prev
        prev.next = None
        self.tail = None
        self.tail = prev
        return ret_key

    def print_front_to_back(self):
        tmp = self.head
        print('Front to Back ', end=' ')
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.next
        print('')

    def print_back_to_front(self):
        print('Back to  Front ', end=' ')
        tmp = self.tail
        while tmp is not None:
            print(tmp.data, end=' ')
            tmp = tmp.prev
        print('')

    def move_to_front(self, node):
        if self.head is None:
            raise KeyError ('Invalid node entry') 
       
        # if first node then return 
        if node.prev is None:
            return

        # if this is last node
        if node.next is None:
            self.tail = node.prev

        # remove this node from dll first
        prev = node.prev
        next = node.next
        prev.next = next
        # if not the last node
        if next:
            next.prev = prev
       
        # add this node in the front of the dll 
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def revese(self):
        pass

def main():
    # linked list program without using inbuilt list() ds
    dlist = DList()
    dlist.push(40)
    node = dlist.push(30)
    dlist.push(20)
    dlist.push(10)
    dlist.append(100)
    dlist.append(200)
    dlist.print_front_to_back()
    dlist.remove_from_last()
    dlist.print_front_to_back()
    dlist.remove_from_last()
    dlist.print_front_to_back()
    print("move {0} to front.".format(node.data))
    dlist.move_to_front(node)
    dlist.print_front_to_back()
    #print(node, node.data)

    #dlist.print_back_to_front()

    '''
    #linked list program by using inbuilt list() ds
    dlist = list()
    dlist.insert(0, 40)
    dlist.insert(0, 30)
    dlist.insert(0, 20)
    dlist.insert(0, 10)
    dlist.append(100)
    dlist.append(200)
    print(dlist)
    dlist.reverse()
    print(dlist)
    '''

if __name__ == "__main__":
    main()
