arr = [-1 for i in range(26)]
S = input()
cnt = 0
for i in S:
    if arr[ord(i) - 97] == -1:
        arr[ord(i) - 97] = cnt
    cnt += 1

for i in arr:
    print(str(i) + " ", end = "")
