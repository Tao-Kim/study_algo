def solution(triangle):
    
    for i, floor in enumerate(triangle):
        if i == 0:
            continue
        for j, num in enumerate(floor):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
                
    return max(triangle[-1])

    """
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/43105
시간 : 14분


다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
-
"""