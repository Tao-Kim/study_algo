def solution(record):
    user = {}
    answer = []

    for task in record:
        temp = task.split()

        if temp[0] in ["Change", "Enter"]:
            user[temp[1]] = temp[2]

    for task in record:
        temp = task.split()
        if temp[0] == "Enter":
            answer.append(f"{user[temp[1]]}님이 " + "들어왔습니다.")
        elif temp[0] == "Leave":
            answer.append(f"{user[temp[1]]}님이 나갔습니다.")

    return answer

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42888
시간 : 13:19
테스트 : 32/32

- 
다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
-
"""