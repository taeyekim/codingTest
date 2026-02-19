import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        
        dfs(x+1, y)
        dfs(x+1, y-1)
        dfs(x, y-1)
        dfs(x-1, y-1)
        dfs(x-1, y)
        dfs(x-1, y+1)
        dfs(x, y+1)
        dfs(x+1, y+1)
        
        return True
    return False

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                cnt += 1
    print(cnt)