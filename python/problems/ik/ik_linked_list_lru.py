'''
LRUCache
    capacity
    size
    put
    get
dll:
   dlist_add_to_front
   dlist_move_to_front
   remove_from_back
get()
                    [ EXISTS ? ]
                      /     \
               NO   /         \ YES
                  /             \
                /                 \
              /                     \
            /                         \
        done                    node = get_dll_node(key)
                                dlist_move_to_front(node)
                                return value
                                eone

put()
                                            [ EXISTS ? ]
                                              /     \
                                       NO   /         \ YES
                                          /             \
                                        /                 \
                                      /                     \
                                    /                         \
                            [ size < capacity? ]        node = get_dll_node(key)   
                            /     \                     dlist_move_to_front(node) 
                          /         \                   done                
                   NO   /             \ YES        
                      /                 \         
                    /                     \      
                  /                         \   
node = dlist_add_to_front(key)                            
add_to_hash(key, (value, node))                          
size 
done                                                     
                                                                                 
'''
from dlist import DList

class LRUCache:
    '''
    Class to implement Least Recently Used (LRU) LRUCache
    '''
    def __init__(self, capacity):
        ''' Constructor '''
        self.hash_map = {}
        self.size = 0
        self.capacity = capacity
        self.dlist = DList()

    def get_dll_node(self, key):
        ''' return the dll node '''
        if key not in self.hash_map:
            raise KeyError('Key not found.')

        return self.hash_map[key][1]

    def add_to_hash(self, key, value, node):
        ''' add a new entry in the hashmap.'''
        self.hash_map[key] = (value, node)

    ''' DLL operations '''
    """
    def dlist_add_to_front(self, key):
        ''' add an entry in the front of the dll '''
        node = self.dlist.push(key)
        return node

    def dlist_move_to_front(self, node):
        ''' Move the dll entry to the front '''
        self.dlist.move_to_front(node)

    def remove_from_last(self):
        ''' Remove the last entry of the dll '''
        return self.dlist.remove_from_last()
    """

    ''' Public apis '''
    def get(self, key):
        ''' Return the cache entry if found '''
        if key not in self.hash_map:
            #raise KeyError('Key not found.')
            return -1

        node = self.get_dll_node(key)
        self.dlist.move_to_front(node)
        return self.hash_map[key][0]

    def put(self, key, value):
        ''' Add the entry in the cache. '''
        if key not in self.hash_map:
            if self.size < self.capacity:
                node = self.dlist.push(key)
                self.add_to_hash(key, value, node)
                self.size += 1
            else:
                ret_key = self.dlist.remove_from_last() 
                print ("lru", ret_key)
                if ret_key in self.hash_map:
                    del self.hash_map[ret_key]
                node = self.dlist.push(key)
                self.add_to_hash(key, value, node)
        else:
            node = self.get_dll_node(key)
            self.dlist.move_to_front(node)
            self.add_to_hash(key, value, node)
        print ("null")

def main():
    ''' start here .. '''
    print("inside main")
    cache = LRUCache(capacity=1)
    cache.put(key=2, value=1)
    cache.put(key=2, value=1)
    print(cache.get(key=2))
    cache.put(key=3, value=2)
    cache.dlist.print_front_to_back()
    print (cache.hash_map)
    print(cache.get(key=2))

if __name__ == "__main__":
    main()

# end of file
