n, k = map(int, input().split())
listA = sorted(list(map(int, input().split())))
listC = sorted(list(map(int, input().split())) + listA[0:k], reverse=True)
print(sum(listA[k:])+sum(listC[0:k]))

    
"""
문제 : p182_두배열의원소교체
시간 : 8분

접근 :
먼저 배열A를 정렬한 후 가장 낮은 k개의 리스트를 배열B에 합친후 내림차순으로 정렬하여
배열A의 나머지 값들과 배열 B의 가장 큰 k개의 값을 합함
-but listC를 정렬하는 과정에서 배열의 길이가 n + k가 되므로 시간복잡도가 (n+k)log n+k가 됨 

다른 사람 풀이 :
========================================================================================
해설 : 각자 배열 정렬 후 비교하여 교체한 방법

n, k = map(int, input().split()) # N과 K를 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력
========================================================================================

노트 :
- 
"""