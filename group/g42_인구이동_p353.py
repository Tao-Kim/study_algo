def find_parent(location):
    i, j = location
    if parent_list[i][j] == location:
        return location
    else:
        parent_list[i][j] = find_parent(parent_list[i][j])
        return parent_list[i][j]

def merge_parent(location_a, location_b):
    if find_parent(location_a) == find_parent(location_b):
        return
    else:
        i_a, j_a = location_a
        i_b, j_b = location_b
        if i_a < i_b:
            parent_list[i_b][j_b] = location_a
        elif i_a > i_b:
            parent_list[i_a][j_a] = location_b
        else:
            if j_a < j_b:
                parent_list[i_b][j_b] = location_a
            else:
                parent_list[i_a][j_a] = location_b

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, min_difference, max_difference = map(int, input().split())

map_list = [list(map(int, input().split())) for _ in range(n)]
parent_list = None


check_end = True
count = 0

while check_end:
    parent_list = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            parent_list[i].append((i, j))

    check_end = False
    checked_list = [[False] * n for _ in range(n)]
    check_stack = []

    for i in range(n):
        for j in range(n):
            if checked_list[i][j]:
                continue

            check_stack.append((i, j))
            group_list = [(i, j)]

            while check_stack:
                k, l = check_stack.pop()
                checked_list[k][l] = True

                for m in range(4):
                    next_k = k + dx[m]
                    next_l = l + dy[m]

                    if 0 <= next_k < n and 0 <= next_l < n and not checked_list[next_k][next_l]:
                        if min_difference <= abs(map_list[k][l] - map_list[next_k][next_l]) <= max_difference:
                            merge_parent((k, l), (next_k, next_l))
                            check_stack.append((next_k, next_l))
                            group_list.append((next_k, next_l))

            if len(group_list) > 1:
                check_end = True
                group_sum = 0
                for k, l in group_list:
                    group_sum += map_list[k][l]

                group_average = group_sum // len(group_list)

                for k, l in group_list:
                    map_list[k][l] = group_average

    if check_end:
        print(parent_list)
        count += 1

print(count)

"""
문제 : p353_인구이동
시간 : xx분

접근 :
- 다시풀기


다른 사람 풀이 :
========================================================================================

========================================================================================


노트 : 
- 
"""
