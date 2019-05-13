import heapq


def get_skyline(buildings):
    heights = []
    for b in buildings:
        heights.append([b[0], -b[2]])
        heights.append([b[1], b[2]])
    heights.sort(key=lambda x: (x[0], x[1]))

    pq = [0]
    prev = 0
    result = []
    for h in heights:
        if h[1] < 0:
            heapq.heappush(pq, (h[1]))
        else:
            pq.remove(-h[1])
            heapq.heapify(pq)
        cur = pq[0]
        if cur != prev:
            result.append([h[0], -cur])
            prev = cur
    return result


# start, end, height
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print (get_skyline(buildings))
#result = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
