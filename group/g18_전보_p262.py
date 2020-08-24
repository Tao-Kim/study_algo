import heapq
import sys
input = sys.stdin.readline

INFINITY = 987654321

n, m, c = map(int, input().split())

datas = [list() for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    datas[x].append((y, z))

times = [INFINITY] * (n + 1)
heap = []

times[c] = 0
heapq.heappush(heap, (0, c))

while heap:
    time, cur = heapq.heappop(heap)

    if times[cur] < time:
        continue
    else:
        for data in datas[cur]:
            calTime = time + data[1]

            if calTime < times[data[0]]:
                times[data[0]] = calTime
                heapq.heappush(heap, (calTime, data[0]))
            

count = 0
max = 0

for time in times:
    if time < INFINITY:
        count += 1
        if max < time:
            max = time

print(count -1, max)

"""
문제 : p262_전보
시간 : 41분

접근 :
문제의 접근과 문제의 입력 조건을 보고 바로 다익스트라 알고리즘을 떠올렸으나
다익스트라 알고리즘 구현이 생각이 안나 거의 해설을 참고해서 작성함


다른 사람 풀이 :
========================================================================================
해설 :
========================================================================================

노트 :
- 다익스트라 알고리즘 정리 및 외우기
"""