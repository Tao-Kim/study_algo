import sys
import copy
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

m_map = [list(map(int, input().split())) for _ in range(n)]

def count_safe_room(m_map_for_solve):
    m_map_for_dfs = copy.deepcopy(m_map_for_solve)
    for i in range(n):
        for j in range(m):
            if m_map_for_solve[i][j] == 2:
                m_map_for_dfs = spread_birus(m_map_for_dfs, i, j)

    count = 0
    for i in range(n):
        for j in range(m):
            if m_map_for_dfs[i][j] == 0:
                count += 1

    return count

def spread_birus(m_map_for_dfs, i, j):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    m_stack = []
    for k in range(4):
        next_i = i + di[k]
        next_j = j + dj[k]

        if 0 <= next_i < n and 0 <= next_j < m:
            m_stack.append((next_i, next_j))

    while m_stack:
        i, j = m_stack.pop()
        if m_map_for_dfs[i][j] == 1 or m_map_for_dfs[i][j] == 2:
            continue
        else:
            m_map_for_dfs[i][j] = 2
            for k in range(4):
                next_i = i + di[k]
                next_j = j + dj[k]

                if 0 <= next_i < n and 0 <= next_j < m:
                    m_stack.append((next_i, next_j))

    return m_map_for_dfs

def solution():
    safe_room_list = []
    for i in range(n):
        for j in range(m):
            if m_map[i][j] == 0:
                safe_room_list.append((i, j))

    combinations_list = combinations(safe_room_list, 3)
    max_safe_room = 0

    for combination in combinations_list:
        m_map_for_solve = copy.deepcopy(m_map)

        for i, j in combination:
            m_map_for_solve[i][j] = 1

        max_safe_room = max(max_safe_room, count_safe_room(m_map_for_solve))

    print(max_safe_room)

solution()

"""
문제 : p341_연구소
시간 : 45분

접근 :
- 조합으로 가능한 모든 경우에 대해 dfs 방식으로 수를 세서 답을 구함


다른 사람 풀이 :
========================================================================================

========================================================================================


노트 : 
- 디버깅하는데 시간을 너무 많이 쓴거 같음, 코드 좀더 꼼꼼히 작성할 것
"""

