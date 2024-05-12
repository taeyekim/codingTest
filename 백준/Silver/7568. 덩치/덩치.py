N = int(input())
arr = []
answer = []
# 키, 몸무게 데이터 수집 후 arr에 저장
for i in range(N):
    element = list(map(int, input().split()))
    arr.append(element)
# 사람 별 덩치 비교, 본인보다 덩치 큰 사람 n명일 시 1 + n으로 등수 매기기
for i in range(N):
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    answer.append(cnt)

print(*answer)