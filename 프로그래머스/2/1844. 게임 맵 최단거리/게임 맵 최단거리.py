from collections import deque

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(h, w, maps, dist):
    q = deque()
    q.append((0, 0))
    dist[0][0] = 1
    
    while q:
        x, y = q.popleft()
        if x == h-1 and y == w-1:
            return dist[x][y]
        
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= h-1 and 0 <= ny <= w-1:
                if maps[nx][ny] == 1 and dist[nx][ny] == 0:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    return -1

def solution(maps):

    h, w = len(maps), len(maps[0])
    dist = [[0] * w for _ in range(h)]
    
    answer = bfs(h, w, maps, dist)
    return answer