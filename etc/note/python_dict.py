"""
dict
https://wikidocs.net/16
"""
#선언
d1 = dict()
d2 = {}
d3 = {'a':1,'b':2}


# 요소 추가
d3['c'] = 3


# 요소 삭제 A(1) W(n)
del d3['c']
d3.pop('c')

# 키로 값 가져오기 A(1) W(n)
d3['a'] # 없으면 애러 발생
d3.get('a') # 없으면 None


# in A(1) W(n)
'a' in d3

# 길이
len(d3) # O(1)

# 키 반환
d3.keys() # for in문과 같은 iterator로 사용 가능하지만 list로 사용시(가령 인덱싱)  list(d3.keys()) 해야함

# 값 반환
d3.values() # 키와 같음

# 키, 값 쌍으로 반환
d3.items() # 키와 같음

'''
정렬 1
'''
target = {
    1: 2,
    3: 1,
    2: 6,
    4: 5,
    5: 3
}

a = sorted(target.items(), key=lambda x:x[0])

print(a)
# [(1, 2), (2, 6), (3, 1), (4, 5), (5, 3)]




'''
정렬 2
'''
target = {
    1: [1, 2],
    3: [3, 1],
    2: [2, 6],
    4: [4, 5],
    5: [3, 3]
}

a = sorted(target.items(), key=lambda x:(x[1][0], -x[1][1]))

print(a)

# [(1, [1, 2]), (2, [2, 6]), (5, [3, 3]), (3, [3, 1]), (4, [4, 5])]
"""
Counter
"""
from collections import Counter
counter = Counter([1, 1, 1, 1, 2, 2, 3, 4, 5])
print(counter[1]) # 4
print(dict(counter)) # {1: 4, 2: 2, 3: 1, 4: 1, 5: 1}
print(counter.most_common(1)) # [(1, 4)]
print(counter.most_common(2)) # [(1, 4), (2, 2)]

