def solution(s):
    lst = s.split(" ")
    total = 0
    for i in range(0, len(lst)):
        if lst[i] == "Z":
            total -= int(lst[i - 1])
        elif lst[i] != "Z":
            total += int(lst[i])
    return total