# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    count_set = set()
    for num in A:
        if num in count_set:
            count_set.remove(num)
        else:
            count_set.add(num)

    return count_set.pop()

"""
문제주소 : https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/start/
시간 : 7분


다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
-
"""