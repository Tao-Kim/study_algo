n, m = map(int, input().split())
parentTable = [i for i in range(n+1)]

def findParent(a):
    if parentTable[a] != a:
        parentTable[a] = findParent(parentTable[a])
        return parentTable[a]
    else:
        return a

def unionTeam(a, b):
    if a < b :
        parentTable[b] = a
    else:
        parentTable[a] = b

for _ in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:
        unionTeam(findParent(a), findParent(b))
    
    elif operation == 1:
        if findParent(a) == findParent(b):
            print("YES")
        else:
            print("NO")
