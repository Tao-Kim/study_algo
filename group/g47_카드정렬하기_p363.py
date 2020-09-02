import heapq

n = int(input())
num_heap = []

for _ in range(n):
    heapq.heappush(int(input()))


sum_of_total_merge = 0

while num_heap:
    num_first = heapq.heappop(num_heap)

    if not num_heap:
        print(sum_of_total_merge)
        break

    num_second = heapq.heappop(num_heap)
    sum_of_first_and_second = num_first + num_second
    heapq.heappush(num_heap, sum_of_first_and_second)
    sum_of_total_merge += sum_of_first_and_second

    """
    문제 : p363_카드 정렬하기
    시간 : 7분

    접근 :
    - 가장 작은 수 끼리 합치면 최소 비교 횟수가 되는 규칙을 이용하여
    힙에 계속 넣어가며 합침
    - 해설과 개념 같음


    다른 사람 풀이 :
    ========================================================================================

    ========================================================================================

    노트 : 
    - 
    """
