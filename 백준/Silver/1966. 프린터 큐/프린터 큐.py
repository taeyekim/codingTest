T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # 문서의 개수, 인쇄 순서 궁금한 문서 큐에서의 인덱스
    joongyodo = list(map(int, input().split())) # 중요도 리스트
    visited = [0 for _ in range(N)] # 해당 문서가 인쇄됐는지 여부를 확인하는 리스트
    visited[M] = 1 # 궁금한 문서 표시
    cnt = 0

    while True:
        if joongyodo[0] == max(joongyodo):
            cnt += 1
            if visited[0] == 1: # 궁금한 문서가 맨 앞에 있을 경우
                print(cnt)
                break
            else:
                joongyodo.pop(0)
                visited.pop(0)
        else:
            joongyodo.append(joongyodo.pop(0))
            visited.append(visited.pop(0))