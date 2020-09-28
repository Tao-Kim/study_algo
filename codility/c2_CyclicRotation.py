# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return []

    K = K % len(A)
    return A[len(A) - K:] + A[:len(A) - K]

"""
문제주소 : https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/start/
시간 : 9분


다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
-
"""