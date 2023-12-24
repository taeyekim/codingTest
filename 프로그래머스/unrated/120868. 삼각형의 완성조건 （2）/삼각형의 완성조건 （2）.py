def solution(sides):
    cnt = 0
    sides.sort()
    for i in range(1, sum(sides)):
        arr = sides[:]
        arr.append(i)
        if arr[1] <= arr[2] and arr[0] + arr[1] > arr[2]:
            cnt += 1
        elif arr[1] >= arr[2] and arr[0] + arr[2] > arr[1]:
            cnt += 1
    return cnt