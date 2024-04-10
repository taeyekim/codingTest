from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(col, row, fire_pos_list):
    q = deque()
    q.append([col, row, 1])
    fq = deque()
    for fc, fr in fire_pos_list:
        fq.append([fc, fr])

    while True:
        fq_len = len(fq)
        for _ in range(fq_len):
            fy, fx = fq.popleft()
            for i in range(4):
                nfy = fy + dy[i]
                nfx = fx + dx[i]
                if 0 <= nfy <= h - 1 and 0 <= nfx <= w - 1:
                    if lst[nfy][nfx] != '#' and lst[nfy][nfx] != '*':
                        lst[nfy][nfx] = '*'
                        fq.append([nfy, nfx])

        q_len = len(q)
        for _ in range(q_len):
            y, x, cnt = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny <= h - 1 and 0 <= nx <= w - 1:
                    if lst[ny][nx] == '.':
                        lst[ny][nx] = cnt
                        q.append([ny, nx, cnt + 1])
                else:
                    return cnt
        # for i in range(C):
        #     print(lst[i])
        # print()
        if not q:
            return "IMPOSSIBLE"
T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    lst = [list(input()) for _ in range(h)]
    fire_pos = []
    for r in range(w):
        for c in range(h):
            if lst[c][r] == '@':
                sc, sr = c, r
            elif lst[c][r] == '*':
                fire_pos.append([c, r])

    answer = bfs(sc, sr, fire_pos)
    print(answer)