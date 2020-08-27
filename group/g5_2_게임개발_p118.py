def turnLeft():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1

n, m = map(int, input().split())
y, x, d = map(int, input().split())
mapTable = []

for _ in range(n):
    mapTable.append(list(map(int, input().split())))

leftStep = [(-1, 0), (0, -1), (1, 0), (0, 1)]
backStep = [(0, 1), (-1, 0), (0, -1), (1, 0)]

checkFourDirection = 0
count = 1
mapTable[y][x] = 2

while True:
    if checkFourDirection == 4:
        afterX = x + backStep[d][0]
        afterY = y + backStep[d][1]
        if 0 <= afterX < m and 0 <= afterY < n:
            if mapTable[afterY][afterX] == 1:
                break
            else:
                y = afterY
                x = afterX
                checkFourDirection = 0
    
    else:
        afterX = x + leftStep[d][0]
        afterY = y + leftStep[d][1]
        if 0 <= afterX < m and 0 <= afterY < n:
            if mapTable[afterY][afterX] == 0:
                mapTable[afterY][afterX] = 2
                y = afterY
                x = afterX
                checkFourDirection = 0
                count += 1
                turnLeft()
                
            else:
                checkFourDirection += 1
                turnLeft()


print(count)

"""
문제 : p118_게임개발
시간 : 측정안함

접근 :

다른 사람 풀이 :
========================================================================================

========================================================================================
노트 :
g5_2 복습하기
"""