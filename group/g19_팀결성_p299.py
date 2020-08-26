def unionTeam(studentA, studentB):
    parentA = parentTable[studentA]
    parentB = parentTable[studentB]
    if parentA != parentB:
        if parentA < parentB:
            parentTable[parentB] = parentA
        else:
            parentTable[parentA] = parentB

def findParent(student):
    if parentTable[student] != student:
        parentTable[student] = findParent(parentTable[student])
    else:
        return student

n,m = map(int, input().split()) #n =0...n 학생번호 m = 연산의 갯수
parentTable = [i for i in range(0, n + 1)]

for _ in range(m):
    operation, a, b = map(int, input().split())
    
    if operation == 0:
        unionTeam(a, b)
    elif operation == 1:
        if findParent(a) == findParent(b):
            print("YES")
        else:
            print("NO")


"""
문제 : p298_팀결성
시간 : 18분

접근 :
해설과 개념은 같음.
4번줄에 부모가 다른지 여부 조건을 추가했고,
17번에 부모테이블을 컨프리헨션으로 작성함


다른 사람 풀이 :
========================================================================================
해설 :
========================================================================================

노트 :
- g19 복습하기
"""