n = int(input())
storeList = tuple(map(int, input().split()))


m = int(input())
requestList = tuple(map(int, input().split()))

for item in requestList:
    if item in storeList:
        print("yes", end=' ')
    else:
        print("no", end=' ')





'''
0.99초 list에서 in 탐색
n = int(input())
storeList = tuple(map(int, input().split()))

storeList = list(range(12345678))

m = int(input())
requestList = tuple(map(int, input().split()))

for item in requestList:
    if item in storeList:
        print("yes", end=' ')
    else:
        print("no", end=' ')



1.24초 set에서 in 탐색
n = int(input())
storeList = tuple(map(int, input().split()))

#storeList = set(list(range(12345678)))
storeList = set(list(range(12345678)))

m = int(input())
requestList = tuple(map(int, input().split()))

for item in requestList:
    if item in storeList:
        print("yes", end=' ')
    else:
        print("no", end=' ')


'''
