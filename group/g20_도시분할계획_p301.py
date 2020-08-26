 # n = 집 개수, m = 길 개수, 양방향, 길마다 유지비
 # 마을 두개로 분리, 분리된 마을안 각 두 집은 경로 연결됨, 마을에 집 최소 하나
 # 두 마을 연결 길 전부 제거, 마을 안 모두 연결시키고 유지비 최소

# 마을 분리 ? 
# 마을안 - mst
# mst를 먼저 만들고 가장 큰 간선 제거

import heapq

def unionHouse(houseA, houseB):
    parentA = parentTable[houseA]
    parentB = parentTable[houseB]
    if parentA != parentB:
        if parentA < parentB:
            parentTable[parentB] = parentA
        else:
            parentTable[parentA] = parentB

def findParent(house):
    if parentTable[house] != house:
        parentTable[house] = findParent(parentTable[house])
    return parentTable[house]

n, m = map(int, input().split())
roadHeap = []
parentTable = [i for i in range(0, n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(roadHeap, (c, a, b))

weightList = []

while roadHeap:
    c, a, b = heapq.heappop(roadHeap)

    if findParent(a) != findParent(b):
        unionHouse(a, b)
        weightList.append(c)


print(sum(weightList) - max(weightList))



"""
문제 : p300_도시분할계획
시간 : 31분

접근 :
해설과 개념은 같음.
c값 순으로 정렬하는 부분을 힙을 이용했고,
last 처리하는 부분을 리스트에 담아서 max로 처리함
                                    *낭비한 것 같음


다른 사람 풀이 :
========================================================================================
해설 :
========================================================================================

노트 :
- find 연산의 작동원리를 잘못 파악하고 있었음, g19도 에러가 있음.
- g19 수정하기
- g20 복습하기
"""