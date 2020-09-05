def solution(clothes):
    clothes_dict = dict()
    
    for name, kind in clothes:
        if clothes_dict.get(kind):
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 2
            
    clothes_counts = list(clothes_dict.values())

    answer = 1
    for clothes_count in clothes_counts:
        answer *= clothes_count
    
    return answer - 1

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42578
시간 : 25분



다른 사람 풀이 :
========================================================================================
counter와 reduce 활용

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
========================================================================================


노트 :
-
"""