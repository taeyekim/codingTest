# 1 익은 토마토, 0 익지 않은 토마토, -1 토마토 없는 칸
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque
def bfs(pos):
    # global day
    q = deque()
    for ele in pos:
        q.append(ele + [tomato[ele[0]][ele[1]]])
    # visited = list([0] * M for _ in range(N))
    # visited[x][y] = day
    while q:
        v = q.popleft()
        # day += 1
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if 0 <= nx <= N - 1 and 0 <= ny <= M - 1:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[v[0]][v[1]] + 1
                    q.append([nx, ny, tomato[v[0]][v[1]] + 1])
        # for i in range(N):
        #     print(tomato[i])
        # print()

M, N = map(int, input().split()) # 가로 M, 세로 N

tomato = [list(map(int, (input().split()))) for _ in range(N)]
bp = False
day = 0
pos = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            pos.append([i, j])

bfs(pos)

answer = 0
for i in range(N):
    answer = max(answer, max(tomato[i]))
    if tomato[i].count(0) >= 1:
        answer = -1
        break
if answer == -1:
    print(-1)
else:
    print(answer - 1)