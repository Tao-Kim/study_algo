from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

houseList = []
chickenList = []

for i in range(n):
    temp = list(map(int, input().split()))

    for j in range(n):
        if temp[j] == 1:
            houseList.append((i, j))
        elif temp[j] == 2:
            chickenList.append((i, j))


def getDistance(houseX, houseY, chickenX, chickenY):
    return abs(houseX - chickenX) + abs(houseY - chickenY)


def solution():
    distanceList = [[] for _ in range(len(chickenList))]

    for i, chicken in enumerate(chickenList):
        chickenX, chickenY = chicken

        for house in houseList:
            houseX, houseY = house
            distance = getDistance(houseX, houseY, chickenX, chickenY)
            distanceList[i].append(distance)


    selectChickenList = list(combinations(range(len(chickenList)), m))
    minDistances = 987654321
    

    for select in selectChickenList:
        sumDistances = 0
        
        for i in range(len(houseList)):
            minDistance = 987654321
            
            for chiken in select:
                minDistance = min(minDistance, distanceList[chiken][i])

            sumDistances += minDistance

        minDistances = min(minDistances, sumDistances)

    print(minDistances)


solution()


"""
문제 : p332_치킨 배달
시간 : 34분 30초

접근 :
- 규칙이나 로직을 찾으려 했으나 쉽게 생각나지 않았고 입력 범위가 적은 점을 이용해서 모두 구현해서 품
- 해설과 풀이 개념은 같으나 미리 모든 거리를 구해두고 계산한 점이 다름

다른 사람 풀이 :
========================================================================================

========================================================================================


노트 : 
- 입력 범위가 적고, 로직이 복잡한 경우 구현 문제로 판별할 필요 있음
"""


