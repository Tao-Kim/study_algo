def solution(participant, completion):
    participant_dict = dict(zip(participant, [0]*len(participant)))
    for name in participant:
        participant_dict[name] += 1
        
    for name in completion:
        participant_dict[name] -= 1
        
    for player, num in participant_dict.items():
        if num == 1:
            return player

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42576
시간 : 15분

- 효율성 테스트가 중요헀던 문제로
- list의 remove는 초과
- set을 이용한 반복문 내 in 초과



다른 사람 풀이 :
========================================================================================
Counter 이용

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
========================================================================================
Counter 이용2
from collections import Counter
def solution(participant, completion):

    inter = list((Counter(participant) - Counter(completion)).elements())

    return inter.pop()
========================================================================================

노트 :
- https://dev.plusblog.co.kr/42 살펴보기
- https://wiki.python.org/moin/TimeComplexity 살펴보기
- 파이썬 Counter 찾아보기
"""