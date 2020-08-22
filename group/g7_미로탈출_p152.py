
def solveMaze(x, y, weight):
    weight -= 1
    if x < 0 or x >= m or y < 0 or y >= n or maze[y][x] == 0 or (maze[y][x] != 1 and maze[y][x] >= weight):
        return
    else :
        maze[y][x] = weight
        solveMaze(x-1, y, weight)
        solveMaze(x+1, y, weight)
        solveMaze(x, y-1, weight)
        solveMaze(x, y+1, weight)
        

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

solveMaze(0, 0, 0)
print(-maze[n-1][m-1])

"""
문제 : p152_미로탈출
시간 : 28분

접근 :
미로를 완전탐색하되 가중치를 두고 가장 짧은 동선의 값을 2차원 리스트에 입력하고
가장 짧은 경우에만 계속 진행시킴


다른 사람 풀이 :
========================================================================================
해설 : bfs로 푼 방법
bfs로 풀 경우 가중치가 자동으로 처리 됨

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))
========================================================================================

노트 :
- 가중치를 두며 완전탐색할때 bfs로 접근하면 가중치 처리가 더 편할 수도 있음
- dfs/bfs 문제 풀이 속도 오래걸림 많이 풀어볼 것
"""