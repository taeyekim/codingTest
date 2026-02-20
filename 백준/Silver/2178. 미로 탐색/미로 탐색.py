import sys
from collections import deque

DIRS = ((1,0), (0,1), (-1, 0), (0, -1))

def bfs(x, y):

    q = deque()
    q.append((x, y))
    dist[x][y] = 1
    
    while q:
        x, y = q.popleft()
        
        if x == n - 1 and y == m - 1:
            print(dist[x][y])
            break
        
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                if grid[nx][ny] == 1 and dist[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

n, m = map(int, sys.stdin.readline().split())

grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]
bfs(0, 0)
