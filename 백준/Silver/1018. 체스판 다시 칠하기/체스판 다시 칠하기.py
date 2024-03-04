
def minV(lst, N, M):

    answer = N*M
    for k in range(N - 7):
        for l in range(M - 7):
            # print(k, k+7, l, l + 7)
            cnt = 0
            cnt2 = 0
            for i in range(k, k+8):
                for j in range(l, l+8):
                    if i % 2 == 0:
                        if j % 2 == 0 and lst[i][j] == 'B':
                            cnt += 1
                        elif j % 2 == 1 and lst[i][j] == 'W':
                            cnt += 1
                    else:
                        if j % 2 == 0 and lst[i][j] == 'W':
                            cnt += 1
                        elif j % 2 == 1 and lst[i][j] == 'B':
                            cnt += 1

            # print(cnt)
            for i in range(k, k+8):
                for j in range(l, l+8):
                    if i % 2 == 0:
                        if j % 2 == 0 and lst[i][j] == 'W':
                            cnt2 += 1
                        elif j % 2 == 1 and lst[i][j] == 'B':
                            cnt2 += 1
                    else:
                        if j % 2 == 0 and lst[i][j] == 'B':
                            cnt2 += 1
                        elif j % 2 == 1 and lst[i][j] == 'W':
                            cnt2 += 1
            # print(cnt2)
            answer = min(cnt, cnt2, answer)
    print(answer)

N, M = map(int, input().split())
lst = [input() for _ in range(N)]

minV(lst, N, M)