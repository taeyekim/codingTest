K, N, M = map(int, input().split()) # 과자 1개 K, 과자 개수 N, 가진 돈 M, ans 부모님께 받아야 하는 모자란 돈

cost = K * N
if M > cost:
    print(0)
else:
    print(cost - M)