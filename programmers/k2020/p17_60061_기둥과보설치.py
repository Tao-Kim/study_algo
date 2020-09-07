n = None
table = None

def is_possible(build):
    x, y, a, b = build
    
    if b == 0: # 삭제
        can_delete = True
        temp = table[y][x]
        if table[y][x] == 2:
            if a == 0:
                table[y][x] = 1
            else:
                table[y][x] = 0
        else:
            table[y][x] = -1
            
       # print(table)
        for i in range(n+1):
            for j in range(n+1):
                if table[i][j] == 0:
                    if not is_possible((j, i, 0, 1)):
                        can_delete = False
                if table[i][j] == 1:
                    if not is_possible((j, i, 1, 1)):
                        can_delete = False
                if table[i][j] == 2:
                    if not is_possible((j, i, 0, 1)) or not is_possible((j, i, 1, 1)):
                        can_delete = False
        table[y][x] = temp
        return can_delete
            
        
    else: # 설치
        if a == 0: # 기둥
            if y < n and (y == 0 or table[y][x] in [1,2] or (x - 1 >= 0 and table[y][x - 1] in [1,2]) or (y - 1 >= 0 and table[y - 1][x] in [0,2])):
                return True
            else:
                return False
        else: # 보
            if (y -1 >= 0 and table[y - 1][x] in [0,2]) or (y - 1 >= 0 and x + 1 <= n and table[y - 1][x + 1] in [0,2]) or (x - 1 >= 0 and table[y][x - 1] in [1,2] and x + 1 <= n and table[y][x + 1] in [1,2]):
                return True
            else:
                return False
            

def solution(_n, build_frame):
    global n
    n = _n
    global table
    table = [[-1] * (n+1) for _ in range(n+1)]
    
    for build in build_frame:
        x, y, a, b = build
        if is_possible(build):
            if b == 0:
                if table[y][x] == 2:
                    if a == 0:
                        table[y][x] = 1
                    else:
                        table[y][x] = 0
                else:
                    table[y][x] = -1
            elif b == 1:
                if table[y][x] == -1:
                    table[y][x] = a
                else:
                    if a != table[y][x]:
                        table[y][x] = 2
                    
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if table[i][j] == 0 or table[i][j] == 1:
                answer.append([j,i,table[i][j]])
            elif table[i][j] == 2:
                answer.append([j,i,0])
                answer.append([j,i,1])
   # answer.sort()
    print(table)
    return sorted(answer)



"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/60061
시간 : 104:12
테스트 : 23/23

- 디버깅 과정에서 코드가 심각하게 지저분해짐
- 시간이 촉박한게 아니라면 간단하게 나마 정리하면 좋을듯

다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
- 
"""