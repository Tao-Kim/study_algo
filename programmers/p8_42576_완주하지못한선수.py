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

========================================================================================


노트 :
- https://dev.plusblog.co.kr/42 살펴보기
- https://wiki.python.org/moin/TimeComplexity 살펴보기
"""