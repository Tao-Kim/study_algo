def check_balance(s):
    left = 0
    right = 0
    
    for char in s:
        if char == '(':
            left += 1
        else:
            right += 1
    
    if left == right:
        return True
    else:
        return False
    
    
def check_correct(s):
    left_remain = 0
    
    for char in s:
        if char == '(':
            left_remain += 1
        else:
            if left_remain >= 1:
                left_remain -= 1
            else:
                return False
            
    if left_remain == 0:
        return True
    else:
        return False

    
def process(p):
    if len(p) == 0:
        return p
    
    if check_correct(p):
        return p
    
    else:
        u = ''
        v = ''
        u_size = 2
        
        while True:
            u = p[:u_size]
            if check_balance(u):
                v = p[u_size:]
                break
            else:
                u_size += 2
            
        if check_correct(u):
            v = process(v)
            return u + v
        
        else:
            v = process(v)
            temp = '(' + v + ')'
            u = u[1:-1]
            
            for char in u:
                if char == '(':
                    temp += ')'
                else :
                    temp += '('
                    
            return process(temp)
            
    
    
def solution(p):
    return process(p)


"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/60058#
시간 : 37:26
테스트 : 25/25

- 각 과정을 함수로 구현하고 재귀하는 방식으로 작성

다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
- p14 다른 사람 풀이 찾아보기
"""