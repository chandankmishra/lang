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

    def remove_from_last(self):
        if self.tail is None:
            #raise KeyError('ther is no entry to remove.')
            return -1

        ret_key = self.tail.data

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

    def move_to_front(self, node):
        if self.head is None:
            #raise KeyError ('Invalid node entry')
            return -1

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
    
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash_map = {}
        self.size = 0
        self.capacity = capacity
        self.dlist = DList()

    def get_dll_node(self, key):
        ''' return the dll node '''
        if key not in self.hash_map:
            #raise KeyError('Key not found.')
            return -1

        return self.hash_map[key][1]
    
    def add_to_hash(self, key, value, node):
        ''' add a new entry in the hashmap.'''
        self.hash_map[key] = (value, node)
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_map:
            return -1

        node = self.get_dll_node(key)
        self.dlist.move_to_front(node)
        return self.hash_map[key][0]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.hash_map:
            if self.size < self.capacity:
                node = self.dlist.push(key)
                self.add_to_hash(key, value, node)
                self.size += 1
            else:
                ret_key = self.dlist.remove_from_last()
                if ret_key in self.hash_map:
                    del self.hash_map[ret_key]
                node = self.dlist.push(key)
                self.add_to_hash(key, value, node)
        else:
            node = self.get_dll_node(key)
            self.dlist.move_to_front(node)
            self.add_to_hash(key, value, node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
