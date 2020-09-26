import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while True:
        first_food = heapq.heappop(scoville)
        if first_food >= K:
            break

        if scoville:
            second_food = heapq.heappop(scoville)
        else:
            return -1

        mixed_food = first_food + (second_food * 2)
        heapq.heappush(scoville, mixed_food)
        answer += 1

    return answer


"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
시간 : 7분


다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
-
"""