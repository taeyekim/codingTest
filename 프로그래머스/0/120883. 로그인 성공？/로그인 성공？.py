def solution(id_pw, db):
    answer = ''
    if id_pw in db:
        return "login"
    for d in db:
        if id_pw[0] == d[0]:
            return "wrong pw"
        
        
    return "fail"