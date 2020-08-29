# int 1개 입력
n = int(input())

# int 여러개 입력
n, m = map(int, input().spli())

# 문자열 입력 - 정확하게는 한줄 문자열 입력임
s = input()


# 자릿 수가 큰 정수 리스트로 받기
# 1111111111 -> [1, 1, 1, 1, 1, 1, 1, 1]
# 1 1 1 1 일떄 : input().split()을 통해 ['1', '1', '1', '1'] -> map(int, 되는 방식
# 11111 일떄 : input()을 통해 '11111'이 되고 iterable이므로 -> map(int, 되는 방식
list(map(int, input())) 



# 입력 받을 리스트의 갯수와 그 아래 리스트가 나오는 형태
# 3
# 1 1 0
# 1 0 0
# 0 0 0
# 리스트 컴프리헨션 활용해서 한줄로 입력 가능
inputList = [list(input().split()) for i in range(int(input()))]