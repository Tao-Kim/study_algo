n, m = map(int, input().split())
y, x, direction = map(int, input().split())
gameMap = list()
for i in range(n):
    gameMap.append(list(map(int, input().split())))

countDirection = 0
result = 1

while True:
    gameMap[y][x] = 2
    if countDirection == 4:
        if direction == 0:
            if gameMap[y+1][x] == 1:
                break
            else :
                y += 1
                countDirection = 0
        elif direction == 1:
            if gameMap[y][x-1] == 1:
                break
            else :
                x -= 1
                countDirection = 0
        elif direction == 2:
            if gameMap[y-1][x] == 1:
                break
            else :
                y -= 1
                countDirection = 0
        elif direction == 3:
            if gameMap[y][x+1] == 1:
                break
            else :
                x += 1
                countDirection = 0
    if direction == 0:
        countDirection += 1
        direction = 3
        if gameMap[y][x-1] == 0:
            x -= 1
            result += 1
            countDirection = 0
    elif direction == 1:
        countDirection += 1
        direction = 0
        if gameMap[y-1][x] == 0:
            y -= 1
            result += 1
            countDirection = 0
    elif direction == 2:
        countDirection += 1
        direction = 1
        if gameMap[y][x+1] == 0:
            x += 1
            result += 1
            countDirection = 0
    elif direction == 3:
        countDirection += 1
        direction = 2
        if gameMap[y+1][x] == 0:
            y += 1
            result += 1
            countDirection = 0
print(result)


"""
문제 : p118_게임개발
시간 : 35분

접근 :
무한 루프 반복문에 현 방향에 따른 처리문을 if문으로 분기 시켜 메뉴얼 1, 2를 처리하고
4방향 모두 체크 여부를 확인하는 용도의 변수와 if문으로 메뉴얼 3을 처리함
해설과 달리 주어진 맵, 지나간 위치를 나누지 않고 1, 2로 나누어 처리함(최종 바다 구별용)

다른 사람 풀이 :
========================================================================================
해설 코드 일부 발췌 : 방향에 따른 배열 인덱스 변화를 구현할때 x, y를 나누어 처리하는 방법 feat list

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
========================================================================================
함수내에서 global 변수?

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
========================================================================================
노트 :
2차원 배열 인덱스 규칙 찾을때 x, y 나누어 처리하는 방법도 숙지할 것 (위 다른 사람 풀이 참조)
파이썬 global 변수 찾아보기
"""