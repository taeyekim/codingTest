from collections import deque
def dfs(s):
    global visit
    st = []
    st.append(s)
    visit[s] = True

    while st:
        v = st.pop()
        print(v, end = ' ')
        for w in sorted(G[v]):
            if not visit[w]:
                dfs(w)

def bfs(s):
    q = deque()
    q.append(s)
    visited = [False] *(N + 1)
    visited[s] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for w in sorted(G[v]):
            if not visited[w]:
                q.append(w)
                visited[w] = True

N, M, V = map(int, input().split()) # 노드(정점) N, 간선 M, 정점 번호 V 4, 5, 1

A = []
G = [[] for _ in range(N+1)]
for _ in range(M):
    A.append(list(map(int, input().split())))

for i in range((len(A))): # [[1,2], [1,3] .. [3,4]] / 첫 스타트 [1,2]
    G[A[i][0]].append(A[i][1])
    G[A[i][1]].append(A[i][0])

visit = [False] * (N + 1)
dfs(V)
print()
bfs(V)