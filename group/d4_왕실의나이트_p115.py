location = input()
x = ord(location[0]) - 96
y = int(location[1])

result = 0
if x - 2 >= 1 and y - 1 >= 1: result += 1
if x - 2 >= 1 and y + 1 <= 8: result += 1
if x - 1 >= 1 and y - 2 >= 1: result += 1
if x - 1 >= 1 and y + 2 <= 8: result += 1
if x + 1 <= 8 and y - 2 >= 1: result += 1
if x + 1 <= 8 and y + 2 <= 8: result += 1
if x + 2 <= 8 and y - 1 >= 1: result += 1
if x + 2 <= 8 and y + 1 <= 8: result += 1

print(result) 


"""
문제 : p115_왕실의 나이트
시간 : 15분

접근 :
확인해야할 가능 여부가 고정이기에 단순하게 모두 확인해서 전체 횟수를 셈


다른 사람 풀이 :
========================================================================================
전체 경우의 수를 목록으로 정의하여 구현한 방법
  
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
========================================================================================

노트 :
쉬운문제였음에도 좀더 좋은 방법이 있을까? 하는 고민에 시간 소모가 많이 되었다.
때론 무식하게 푸는 방법이 더 효율적일지도 모름.
"""