import math
def solution(progresses, speeds):
    answer = []
    ends = []
    for i in range(len(progresses)):
        ends.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    count = None
    current_day = 0
    
    for end in ends:
        if end > current_day:
            answer.append(count)
            count = 1
            current_day = end
        else:
            count += 1    
    
    answer.append(count)
    answer.pop(0)
    
    return answer

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42586
시간 : 14분


다른 사람 풀이 :
========================================================================================

========================================================================================


노트 :
- 
"""