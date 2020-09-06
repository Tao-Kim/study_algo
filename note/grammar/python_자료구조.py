############# 시간 복잡도 ############
# https://dev.plusblog.co.kr/42
# https://wiki.python.org/moin/TimeComplexity



"""
set
https://wikidocs.net/1015

기본 개념 - 집합
          - 중복x, 순서x인 자료형

           - dict와 같이 hash를 기반으로 작동하기에 시간복잡도가 항상 보장되지 않음

"""
# 선언 O(n)
s1_empty = set()
            #### 안됨 dict 선언 됨 s2_empty = {}
s1 = set([1,2,3])
s2 = {1,2}


#값 1개 추가 O(1)
s1.add(4)

#값 여러개 추가 O(updateList.length)
s1.add([5,6])

# 특정 값 제거 A(1) W(n) 
s1.remove(6)
s1.discard(6) # 없어도 애러 발생안함

#길이 O(1)
len(s1)

# in A(1) W(n)
6 in s1 


# 합집합 O(n+k)
s1 | s2

# 교집합 A(min(n, k)) W(nk)
s1 & s2

# 차집합 O(n)
s1 - s2

# 동일 집합 여부 
s1 == s2
s1 != s2

# 서브셋 여부
s1 <= s2


"""
list
https://wikidocs.net/14
https://github.com/db97828/PythonAlgorithm/blob/master/List.md
"""
a = [1, 2, 3, 4, 5]
del a[1]
print(a) # [1, 3, 4, 5]

a = [1, 2, 3, 4, 5]
del a[2:]
print(a) # [1, 2]


# list.count() : O(n)


#리스트 인덱싱, 할당, 슬라이싱
a[1] = 10 # O(1)
a[1:4]  # O(4-1)

# 리스트 길이 O(1)
len(a)

# 값 추가
a.append(4) # O(1)
a.insert(INDEX, VALUE) # W(n) - insert(0, value) 반복사용하려면 deque쓸 것
a.extend(list_k) # O(k)

# 값 제거
a.remove(VALUE) # 값으로 제거 O(n)
del a[INDEX] # 인덱스로 제거 O(n)
pop(INDEX) # 인덱스로 꺼내기 (제거 및 반환) O(n) - pop(0) 반복사용하려면 deque쓸 것
pop() # 마지막 인덱스 꺼내기 O(1)


# 리스트 같은지 여부 O(n)
a == b

# in O(n)
6 in a

# 리스트 정렬 O(nlogn)
a.sort()

#리스트 뒤집기 O(n)
a.reverse()

# 최대, 최소 합
max(a) # O(n)
min(a) # O(n)
sum(a) # B(n) - 리스트 형태에 따라 다름


# 리스트 선언 응용
#기본 컴프리헨션
a = [i for i in range(5)] # [0, 1, 2, 3, 4]

# 조건문 연계
b = [i for i in range(5) if i % 2 == 0] # [0, 2, 4]

# if else
c = [i if i % 2 == 0 else -i for i in range(5)] # [0, -1, 2, -3, 4]

# enumerate 연계
list_temp = [10, 20, 30, 40, 50]
d = [x for i, x in enumerate(list_temp) if i % 2 == 0] # [10, 30, 50]

# 그 외 
e = [(i,j) for i in range(3) for j in range(3)] # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
f = [(i,j) for i in range(3) if i % 2 == 0 for j in range(3) if j % 2 == 0] # [(0, 0), (0, 2), (2, 0), (2, 2)]


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



"""
Counter
"""
from collections import Counter
counter = Counter([1, 1, 1, 1, 2, 2, 3, 4, 5])
print(counter[1]) # 4
print(dict(counter)) # {1: 4, 2: 2, 3: 1, 4: 1, 5: 1}
print(counter.most_common(1)) # [(1, 4)]
print(counter.most_common(2)) # [(1, 4), (2, 2)]



"""
#스택, 큐. 힙
https://github.com/entimer/AlgorithmStudy/blob/master/%EC%8A%A4%ED%83%9D%EA%B3%BC_%ED%81%90_%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84%ED%81%90.md
"""
#스택 - list 이용
stack = [1,2]

stack.append(3)
value = stack.pop()

# 큐
from collections import deque
queue = deque() # deque([1,2,3]) 가능

queue.append(3)
value = queue.popleft()


# 힙 - heapq 디폴트로 최소힙임
import heapq
heap = []
# 기존 리스트 힙변환
{
    heap2 = [4,1,3,5,6,]
    heapq.heapify(heap2)
}

heapq.heappush(heap, 3)
value = heapq.heappop(heap)

#최대힙
heapq.heappush(heap, -value)
value = -heapq.heapopp(heap)


