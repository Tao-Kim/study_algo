import sys
input = sys.stdin.readline


def findParent(a):
    if parentTable[a] != a:
        parentTable[a] = findParent(parentTable[a])

    return parentTable[a]


def mergeParent(a, b):
    if a < b:
        parentTable[b] = a
    else:
        parentTable[a] = b

n, m = map(int, input().split())
edgeList = []
parentTable = [i for i in range(n+1)]
visitedList = [False for _ in range(n+1)] 

for _ in range(m):
    a, b, c = map(int, input().split())
    edgeList.append((c, a, b))

edgeList.sort()

maxOfEdge = 0
sumOfEdge = 0

for edge in edgeList:
    c, a, b = edge

    parentA = findParent(a)
    parentB = findParent(b)

    if parentA != parentB:
        mergeParent(parentA, parentB)
        maxOfEdge = max(maxOfEdge, c)
        sumOfEdge += c
        
print(sumOfEdge - maxOfEdge)