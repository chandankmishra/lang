def getSkyline(buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    result = []
    height = []
    for b in buildings:
        height.append((b[0], -b[2]))
        height.append((b[1], b[2]))
    height = sorted(height, key=lambda x: [x[0], x[1]])

    pq = [0]
    prev = 0
    for h in height:
        if h[1] < 0:
            heapq.heappush(pq, h[1])
        else:
            pq.remove(-h[1])
            heapq.heapify(pq)
        cur = -pq[0]
        if prev != cur:
            result.append((h[0], cur))
            prev = cur
    return (result)

    ''' NOTES
    Three Edge Cases:
    ================
    1. Start of the two buildings are same: We should process the start with greater height.
    2. End of the two buildings are same: We should process the end with smaller height
    3. End of one build and start of next building is same: We should process the start building first and then end building.

    Solution:
    =========
    To solve these three edge cases first add the start, end and heights in an array as (start, height) and (end, height) pairs.
    Add the start height as negative (this makes start height smaller so it will apear before in PQ-minheap). Then sort array
    based on (x=(start or end), h=height). This way all 3 corner cases listed above will be addressed.

    To solve this problem maintain a PQ of heights only. If we encounter a start (h < 0) then we add height into PQ and if we
    encounter end (h > 0) then remove height from PQ. After the remove we have to heapify the PQ.

    After adding or removing the height if it changes the max value of the PQ (by comparing the prev with final/current max
    height) add the current x (start or end) and height into the final result.

    Time Complexity:
    ================
    - sorting is O(nlogn).
    - add is log(n) and we do add max n times so it is O(nlogn)
    - delete is O(n) to delete and logn to heapify. So for n time delete it will be n*(n + logn) = O(n^2)

    Make Time Complexity for delete O(nlogn):
    =========================================
    To bring the overall time complexity from O(n^2) to O(nlogn) we have to bring the TC of delete from O(n^2) to O(nlogn).
    For that we have to maintain a additional hashmap with key has value and value as index into the heap. Also we need to
    track the end index of the heap. Which can be done via heap size variable. Then for delete
    - replace the element which need to be deleted with the value of the last element
    - reduce the size by 1.
    - Delete the entry from the hash table. These 3 steps will take O(1) time.

    - Heapify the PQ as before, which will take O(logn) time.
    So now n delete will take n * logn => O(nlogn) Time.
    '''
