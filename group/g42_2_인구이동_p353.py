from collections import deque

n, l, r = map(int, input().split())

country_table = []

for i in range(n):
    country_table.append(list(map(int, input().split())))


count = 0
group_count = 0

while True:
    pre_group_count = group_count
    check_map = [[False] * n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            queue.append((i, j))
            cur_count = 0
            cur_total = 0
            group_stack = []

            while queue:
                x, y = queue.popleft()

                if check_map[x][y]:
                    continue
                else:
                    check_map[x][y] = True
                    current = country_table[x][y]
                    cur_count += 1
                    cur_total += current
                    group_stack.append((x, y))

                    if x-1 >= 0 and not check_map[x-1][y] and l <= abs(current - country_table[x-1][y]) <= r:
                        queue.append((x-1, y))
                    if x+1 < n and not check_map[x+1][y] and l <= abs(current - country_table[x+1][y]) <= r:
                        queue.append((x+1,y))
                    if y-1 >= 0 and not check_map[x][y-1] and l <= abs(current - country_table[x][y-1]) <= r:
                        queue.append((x,y-1))
                    if y+1 < n and not check_map[x][y+1] and l <= abs(current - country_table[x][y+1]) <= r:
                        queue.append((x,y+1))
            
            if cur_count > 1:
                group_count += 1
                avg = cur_total // cur_count

                for x, y in group_stack:
                    country_table[x][y] = avg

    if pre_group_count == group_count:
        break



print(group_count)
    
                        




