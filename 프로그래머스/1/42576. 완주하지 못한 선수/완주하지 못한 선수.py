from collections import Counter

def solution(participant, completion):
    answer = ''
    comDict = Counter(completion)
    for p in participant:
        if not comDict[p]:
            answer = p
            break
        comDict[p] -= 1
        if comDict[p] == -1:
            answer = p
            break
    return answer