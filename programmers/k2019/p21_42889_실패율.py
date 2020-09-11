def solution(N, stages):
    fail_count_list = [0] * (N+2)
    total_count_list = [0] * (N+2)

    for stage in stages:
        fail_count_list[stage] += 1

        for stage in range(1, stage+1):
            total_count_list[stage] += 1

    fail_percentage_list = [[fail_count_list[i] / total_count_list[i], i] if total_count_list[i] != 0 else [0, i] for i in range(1, N+1)]
    fail_percentage_list.sort(reverse=True, key=lambda x : [x[0], -x[1]])

    answer = [stage[1] for stage in fail_percentage_list]
    return answer

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42889
시간 : 11:36
테스트 : 27/27

- 테스트 22 〉	통과 (7070.56ms, 17.5MB) 
- N사이즈 리스트를 4개나 생성하고, 거진 N^2 이라 효율 안좋음

다른 사람 풀이 :
========================================================================================
result를 dict로 선언하고 스테이지 단위로 처리한 경우 - 공간

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
    
    
========================================================================================

노트 :
-
"""