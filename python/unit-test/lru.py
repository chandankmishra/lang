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

    def __len__(self):
        return self.size

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key][1]
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
                self.hash_map[key] = (value, node)
                self.size += 1
            else:
                ret_key = self.dlist.remove_from_last()
                if ret_key in self.hash_map:
                    del self.hash_map[ret_key]
                node = self.dlist.push(key)
                self.hash_map[key] = (value, node)
        else:
            node = self.hash_map[key][1]
            self.dlist.move_to_front(node)
            self.hash_map[key] = (value, node)


def main():
    ''' start here .. '''
    print("inside main")
    cache = LRUCache(capacity=2)
    cache.put(key=2, value=2)
    cache.put(key=3, value=3)
    print("get(2)", cache.get(key=2))
    print("get(3)", cache.get(key=3))
    cache.put(key=3, value=33)
    cache.put(key=4, value=4)
    print("get(3)", cache.get(key=3))
    # cache.dlist.print_front_to_back()
    print (cache.hash_map)
    print(cache.get(key=2))


if __name__ == "__main__":
    main()
