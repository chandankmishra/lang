def build_path(backref, r, c, keyRing):
    path =[]  
    current = r, c, keyRing
    while current:
        brow, bcolumn, bkey = current
        path.append((brow, bcolumn))
        current = backref[current]
    return path[::-1]

def get_start_index(grid, m, n):
    start_r, start_c = -1, -1
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='@': 
                start_r, start_c = i,j
                break
    return start_r, start_c

def find_shortest_path(grid):
    m = len(grid)
    n = len(grid[0])
    start_r, start_c = get_start_index(grid, m, n) 

    q = []
    q.append((start_r,start_c, 0))
    
    # create a set with hashmap as keys. hash map will have r,c as keys and set of keychain as values
    # seen could have (r,c,keychain) as key but this will duplicate r,c for different keychains
    seen = {(r,c):set() for r in range(m) for c in range(n)}
    seen[(start_r,start_c)].add(0)
    
    backref = {(start_r, start_c, 0): None} 

    while q:
        r, c, keyRing = q.pop(0)
        if grid[r][c]=='+':
            return build_path(backref, r, c, keyRing)

        for rr, cc, n_keyRing in get_neighbours(grid, r, c, keyRing):
            if not isVisited(rr, cc, n_keyRing, seen): 
                q.append((rr, cc, n_keyRing))
                backref[(rr, cc, n_keyRing)]= r, c, keyRing
                seen[(rr, cc)].add(n_keyRing)
    return []
                    

def isVisited(n_r, n_c, n_keyRing, seen):
    # not clear why if we just do key lookup in seen[(n_r, n_c)] then causes TLE
    for key in seen[(n_r, n_c)]:
        # not clear why if we just check n_keyRing == key then it gives TLE
        if n_keyRing & key == n_keyRing:
            return True
    return False

def get_neighbours(grid, r, c, keyRing):
    m = len(grid)
    n = len(grid[0])
    DIR = [[0,1],[1,0],[0,-1],[-1,0]]
    res =[]
    for dr, dc in DIR :
        rr, cc = r+dr, c+dc
        if not  (0<=rr<m  and 0<=cc<n):
            continue
        if grid[rr][cc]=='#':
            continue
        if grid[rr][cc] in 'ABCDEFGHIJ' :
            if keyRing  & (1 << (ord(grid[rr][cc])-ord('A'))) == 0:
                continue
        if grid[rr][cc] in 'abcdefghij':
            n_keyRing = keyRing | (1 << (ord(grid[rr][cc])-ord('a')))
        else:
            n_keyRing = keyRing
        res.append((rr, cc, n_keyRing))
    return res
