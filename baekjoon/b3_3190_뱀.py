# == g32

from collections import deque

n = int(input())
board = [[0] * n for _ in range(n)]
board[0][0] = 1
moveQueue = deque()
moveQueue.append((0,0))

k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 2

l = int(input())
turnQueue = deque()
for _ in range(l):
    x, c = input().split()
    turnQueue.append((int(x), c))

turnQueue.append((0, 'Dummy'))
curTime = 0
x, c = turnQueue.popleft()
direction = 0 # 0 - 우 1 - 상 2- 좌 3 - 하
move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
curRow = 0
curCol = 0


def turnLeft():
    global direction
    if direction == 3:
        direction = 0
    else:
        direction += 1

def turnRight():
    global direction
    if direction == 0:
        direction = 3
    else:
        direction -= 1

while True:
    if x == curTime:
        if c == 'L':
            turnLeft()
        elif c == 'D':
            turnRight()
        x, c = turnQueue.popleft()
    
    curTime += 1
    nextRow = curRow + move[direction][0]
    nextCol = curCol + move[direction][1]

    if nextRow < 0 or nextRow >= n or nextCol < 0 or nextCol >= n or board[nextRow][nextCol] == 1:
        print(curTime)
        break

    elif board[nextRow][nextCol] == 0:
        lastRow, lastCol = moveQueue.popleft()
        board[lastRow][lastCol] = 0

    curRow = nextRow
    curCol = nextCol
    board[nextRow][nextCol] = 1
    moveQueue.append((nextRow, nextCol))
        
"""
문제 : p327_뱀
시간 : 26분

접근 :
해설과 풀이 유사
-해설과 달리 전부 전역으로 선언하고 풀이하여 지저분한듯

다른 사람 풀이 :
========================================================================================
방향전환 나누기
def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction




함수로 정리한 형태

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
========================================================================================
import sys
n = int(sys.stdin.readline())
apple = set([tuple(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))])
cmd = [list(sys.stdin.readline().split()) for i in range(int(sys.stdin.readline()))]
snake = [[-2]*n for _ in range(n)]
snake[0][0] = 0
x,y,d = 0,0,0
l = 1
t = 0
idx = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
# print((2,5) in apple)

while True:
    t += 1
    l += 1
    x += dx[d]
    y += dy[d]
    if x < 0 or x >= n or y < 0 or y >= n:
        break
    if snake[x][y] >= t-l+1:
        break
    if (x+1,y+1) in apple:
        apple.remove((x+1,y+1))
    else:
        l -= 1
    snake[x][y]=t

    if idx < len(cmd) and int(cmd[idx][0]) == t:
        if cmd[idx][1] == 'D':
            d = (d+1) % 4
        else:
            d = (d+3) % 4
        idx += 1
print(t)
========================================================================================


노트 : 
- [0, 1, 2, 3] 순환하는 꼴 x = (x + 1) % 4 고려하기
- 로직이 복잡해질거 같으면 함수로 나누기
- g32 다시풀기 (함수로 나누어 풀기)
- g32 풀이2번 다시보기
"""


