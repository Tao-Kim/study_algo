from itertools import combinations
import copy

def check_hide(test_map):
    check_list = []
    for i in range(n):
        for j in range(n):
            if test_map[i][j] == 'S':
                check_list.append((i,j))

    while check_list:
        i, j = check_list.pop()

        i_right = i + 1
        while i < i_right < n:
            if test_map[i_right][j] == 'O':
                break
            elif test_map[i_right][j] == 'T':
                return False
            else:
                i_right += 1

        i_left = i -1
        while 0 <= i_left < i:
            if test_map[i_left][j] == 'O':
                break
            elif test_map[i_left][j] == 'T':
                return False
            else:
                i_left -= 1

        j_bottom = j + 1
        while j < j_bottom < n:
            if test_map[i][j_bottom] == 'O':
                break
            elif test_map[i][j_bottom] == 'T':
                return False
            else:
                j_bottom += 1

        j_top = j - 1
        while 0 <= j_top < j:
            if test_map[i][j_top] == 'O':
                break
            elif test_map[i][j_top] == 'T':
                return False
            else:
                j_top -= 1

    return True

n = int(input())
my_map = [list(input().split()) for _ in range(n)]

x_list = []

for i in range(n):
    for j in range(n):
        if my_map[i][j] == 'X':
            x_list.append((i,j))

combi_list = combinations(x_list, 3)
result_list = []

for combi in combi_list:
    test_map = copy.deepcopy(my_map)

    for i, j in combi:
        test_map[i][j] = "O"

    result_list.append(check_hide(test_map))

if result_list.count(True) != 0:
    print("YES")
else:
    print("NO")