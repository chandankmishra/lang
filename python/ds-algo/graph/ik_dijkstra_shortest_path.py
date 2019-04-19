# Dijkstra Shortest Path Algorithm O(E + Vlog(V))
# Priority Queue interface
# set_priority(key, new_priority) -> None
# get_priority(key, default=None) -> priority
# pop()                           -> (key, priority)
# size()                          -> N


# implement priority queue using HashMap & Heap
class Vertex:
    neighbors = {} #<vertex,weight>

def dijkstra(start, end):
    pq = PriorityQueue()
    pq.set_priority(start, 0)

    exhausted = set()
    back_refs = {}

    while pq.size() > 0:
        v, dist = pq.pop() 
        if v == end:
            return dist

        for next_node, wt in v.neighbours.items():
            if next_node in exhausted:
                continue
            curr_dist = pq.get_priority(next_node, float("inf"))
            if dist + wt < curr_dist:
                back_refs[next_node] = v
                pq.set_priority(next_node, dist + wt)
        exhausted.add(v) 

    if end not in back_refs:
        return None

    # return the path
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = back_refs[curr]
    return path[::-1] #reverse and return

