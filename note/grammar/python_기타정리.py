#---------------------------------------------------------------------------
# 순열과 조합
#---------------------------------------------------------------

# permutations - 순서o, 중복x
from itertools import permutations
data = [1, 2, 3]
result = list(permutations(data, 2))
print(result) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


# combinations - 순서x, 중복x
from itertools import combinations
data = [1, 2, 3]
result = list(combinations(data, 2))
print(result) # [(1, 2), (1, 3), (2, 3)]


# product - 순서o, 중복o
from itertools import product
data = [1, 2, 3]
result = list(product(data, repeat=2))
print(result) # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


# combinations_with_replacement - 순서x, 중복o
from itertools import combinations_with_replacement
data = [1, 2, 3]
result = list(combinations_with_replacement(data, 2))
print(result) # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]




#--------------------------------------------------------------------------------------
# math
#---------------------------------------------------------------------------------------

# math
import math
print(math.factorial(5)) # 팩토리얼
print(math.sqrt(7)) # 제곱근
print(math.gcd(21, 14)) # 최대 공약수
#최대 공배수 : n * m // gcd(n, m)

print(math.ceil(2.3)) # 올림
print(math.floor(2.3)) # 내림 
    {
    print(3 // 2) # 1
    print(5 // 2) # 2
    print(int(3/2)) # 1
    print(int(5/2)) # 2
    }
print(math.rount(2.3)) #반올림 - 정수부가 짝수이면 내림 홀수이면 올림



#--------------------------------------------------------------------------------------
# 이진탐색 bisect
#---------------------------------------------------------------------------------------

# bisect 이진 탐색
from bisect import bisect_left, bisect_right
# bisect_left(list, x) x가 삽입 될 왼쪽 인덱스 반환
# bisect_right(list, x) x가 삽입 될 오른쪽 인덱스 반환
# bisect right - bisect left 로 count 활용가능 O(logN)


#--------------------------------------------------------------------------------------
# map, filter, reduce
#---------------------------------------------------------------------------------------

# map
# iterable 모든 요소에 함수 적용
#map(function, iterable)
print(list(map(max, [[1,2,3],[2,3,4],[4,5,6]])))


# filter
# iterable 모든 요소에 function이 true인 경우만 반환
#filter(function(true, false 반환형), iterable)
print(list(filter(lambda x: x>4, [1,2,3,4,5,6])))


# reduce
# iterable 모든 요소에 누적해서 function 적용
# reduce(

from functools import reduce
print(reduce(lambda x,y : 2*x+y, [2,3,4])) # 시작 x =2, y = 3, (2*(2*2 + 3) + 4)
print(reduce(lambda x,y : x+2*y, [2,3,4])) # 시작 x =2, y = 3,  (2+ 2*3) + 2*4
print(reduce(lambda x,y : x+2*y, [2,3,4], 10)) # 시작 x  =10, y =2, ((10+ 2*2) + 2*3 ) + 2*4


#--------------------------------------------------------------------------------------
# enumerate 
#---------------------------------------------------------------------------------------
a = [1,2,3,4,5]

list(enumerate(a)) # [(0,1), (1,2), (2,3), (3,4), (4,5)]
list(enumerate(a, start=4)) # [(4,1), (5,2), (6,3), (7,4), (8,5)]


#--------------------------------------------------------------------------------------
# any, all
#---------------------------------------------------------------------------------------

a = [1, 2, 3, 4, 0]
b = [True, False]
c = [False, False]

print(any(a)) # True - (1, 2, 3, 4) 때문
print(all(a)) # False - 0 때문
print(any(c)) # False
print(all(c)) # False

print(any([i > 4 for i in range(6)])) # True i에 5들어감
