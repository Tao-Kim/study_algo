def checkFrame(y, x):
    if y < 0 or y >= n or x <0 or x >= m or frame[y][x] != 0:
        return
    else :
        frame[y][x] = 2
        checkFrame(y-1, x)
        checkFrame(y+1, x)
        checkFrame(y, x-1)
        checkFrame(y, x+1) 

n, m = map(int, input().split())
result = 0
frame = []
for i in range(n):
    frame.append(list(map(int, input())))


for i in range(n):
    for j in range(m):
        if frame[i][j] == 0:
            checkFrame(i, j)
            result += 1
            
print(result)


"""
문제 : p149_음료수 얼려먹기
시간 : 19분

접근 :
n * m 전체를 반복하되 현재 좌표에 연결된 구멍이 뚫린 0을 일괄로 처리하며 반복시켜서
카운트 하는 방법으로 품
일괄 처리는 함수를 선언하고 상하좌우 4방향을 재귀하는 방법으로 품


다른 사람 풀이 :
========================================================================================
========================================================================================

노트 :
- list(map(int, input())) : 1111111111 -> [1, 1, 1, 1, 1, 1, 1, 1] 
- 파이썬 input 사용방법 좀더 찾아볼 것
"""