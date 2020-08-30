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




# bisect 이진 탐색
from bisect import bisect_left, bisect_right
# bisect_left(list, x) x가 삽입 될 왼쪽 인덱스 반환
# bisect_right(list, x) x가 삽입 될 오른쪽 인덱스 반환
# bisect right - bisect left 로 count 활용가능 O(logN)



# Counter
from collections import Counter
counter = Counter([1, 1, 1, 1, 2, 2, 3, 4, 5])
print(counter[1]) # 4
print(dict(counter)) # {1: 4, 2: 2, 3: 1, 4: 1, 5: 1}



# math
import math
print(math.factorial(5)) # 팩토리얼
print(math.sqrt(7)) # 제곱근
print(math.gcd(21, 14)) # 최대 공약수
#최대 공배수 : n * m // gcd(n, m)


"""
set
https://wikidocs.net/1015

"""




"""
list
https://wikidocs.net/14
"""
a = [1, 2, 3, 4, 5]
del a[1]
print(a) # [1, 3, 4, 5]

a = [1, 2, 3, 4, 5]
del a[2:]
print(a) # [1, 2]


# list.count() : O(n)


"""
dict
https://wikidocs.net/16
"""
