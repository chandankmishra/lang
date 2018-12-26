def shortest_distance(graph, start, end, seen, recur):
    seen.add(start)
    queue = [[start, 0]]
    while queue:
        cur, d = queue.pop(0)
        recur.add(cur)
        for nxt in list(graph[cur]):
            if nxt in recur:
                continue
            if nxt == end:
                return d + 1
            if nxt not in seen:
                queue.append([nxt, d + 1])
                seen.add(nxt)
        recur.remove(cur)

    return -1


def get_nxt(board, nxt):
    while board[nxt] != -1:
        nxt = board[nxt] - 1
    return nxt


def build_graph(graph, n, board):
    for i in range(n):
        if i not in graph:
            graph[i] = set([])

        if board[i] != -1:
            graph[i].add(get_nxt(board, i))

    for i in range(n):
        if board[i] == -1:
            for j in range(6):
                nxt = i + 1 + j
                if nxt < n:
                    if board[nxt] == -1:
                        graph[i].add(nxt)
                    else:
                        graph[i].add(get_nxt(board, nxt))


def minNumberOfRolls(n, board):
    graph = {}
    build_graph(graph, n, board)
    # print (graph)
    seen = set()
    dist = -1
    for vertex in graph[0]:
        if vertex not in seen:
            dist = shortest_distance(graph, 0, n - 1, seen, set())
    return dist


# driver code
moves = [-1, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
N = len(moves)
print(minNumberOfRolls(N, moves))
