def solution(myString):
    answer = myString.split("x")
    while "" in answer:
        answer.remove("")
    answer.sort()
    return answer