def solution(numbers, n):
    total = 0
    for number in numbers:
        if total + number > n:
            return total + number
        else:
            total += number