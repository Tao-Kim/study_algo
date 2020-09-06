# 리스트 정렬 기본
a = [4, 3, 1, 6]

a.sort() # 반환x, a정렬, default 오름차순
a.sort(reverse=True) # 반환x, a정렬, 내림차순

b = sorted(a) # 반환o
b = sorted(a, reverse=True)


# 정렬 기준 설정

# 요소가 iterable일때
c = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]
d = sorted(d, key = lambda x : x[0])

# 다중 기준으로도 정렬 가능
# 기준에 연산도 가할 수 있음
e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)] 
f = sorted(e, key = lambda x : (x[0], -x[1]))

g = [(1, 3), (-2, 4), (1, 2), (1, 4)]
h1 = sorted(g, key = lambda x: x[0]) # [(-2, 4), (1, 3), (1, 2), (1, 4)]
h2 = sorted(g, key = lambda x: (x[0], x[1])) # [(-2, 4), (1, 2), (1, 3), (1, 4)]
h3 = sorted(g, key = lambda x: (abs(x[0]), x[1])) # [(1, 2), (1, 3), (1, 4), (-2, 4)]



# cmp_to_key - 람다로 표현이 힘든 경우 유용함
from functools import cmp_to_key

def compare(x, y):
	if(x[0] < y[0]): # x[0] 값이 y[0]값 보다 작으면
		return 1 # y 내용을 앞으로 보냄
	elif(x[0] > y[0]):
		return -1
	else: # x[0] 값이 y[0]값과 동일하면
		if(x[1] < y[1]): # x[1]과 y[1]을 비교해서 y[1]이 크면
			return -1 # x 내용을 앞으로 보냄
		elif(x[1] > y[1]):
			return 1
		else:
			return 0

sample = [[4,'c'], [10, 'b'], [13, 'b'], [1, 'd'], [10, 'a']]
print(sorted(sample, key=cmp_to_key(compare)))