from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(col, row):
    q = deque()
    check_sum = 21e9
    visited = [[0] * M for _ in range(N)]
    q.append((col, row, visited))
    visited[0][0] = 1

    while q:
        y, x, v = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny <= N-1 and 0 <= nx <= M-1 and lst[ny][nx] == 1 and v[ny][nx] == 0:
                v[ny][nx] += v[y][x] + 1
                # print(ny, nx, v[ny][nx])
                # for i in range(N):
                #     print(v[i])
                # print()
                if ny == N-1 and nx == M-1:
                    check_sum = min(check_sum, v[ny][nx])
                else:
                    q.append((ny, nx, v))

    return check_sum

N, M = map(int, input().split())

lst = [list(map(int, input())) for _ in range(N)]
answer = bfs(0, 0)
print(answer)