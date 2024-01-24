import copy

def solution(spell, dic):
    for strs in dic:
        cnt = 0
        for s in spell:
            if strs.count(s) == 1:
                cnt += 1
            else:
                break
            if cnt == len(spell):
                return 1
    return 2