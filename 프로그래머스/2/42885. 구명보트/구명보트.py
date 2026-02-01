def solution(people, limit):
    answer = 0
    
    # 사람들 몸무게가 담긴 배열 people, 구명보트 무게 제한 limit
    # 구명보트 최대한 적게 사용하여 탈출
    # 보트 하나당 최대 2인
    # 40 40 50 50 60 60 70 70 80 80 90 90 100 limit 100

    people.sort()
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] > limit:
            right -= 1
        else:
            left += 1
            right -= 1
        answer += 1
            
    return answer