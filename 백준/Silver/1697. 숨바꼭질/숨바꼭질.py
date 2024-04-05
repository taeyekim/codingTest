from collections import deque

def bfs(N, K):
    q = deque()
    q.append((N, 0))
    visited = [False] * 100001
    visited[N] == True
    while q:
        pos, time = q.popleft()
        if pos == K:
            return time

        next_pos = pos * 2
        if 0 <= next_pos <= 100000 and not visited[next_pos]:
            q.append((next_pos, time + 1))
            visited[next_pos] = True

        for c in (pos-1, pos+1):
            if 0 <= c <= 100000 and not visited[c]:
                q.append((c, time + 1))
                visited[c] = True

# 수빈 위치 N, 동생 위치 K
N, K = map(int, input().split())
cnt = 0
answer = bfs(N, K)
print(answer)