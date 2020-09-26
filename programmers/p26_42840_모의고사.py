def solution(answers):
    student_one = [1, 2, 3, 4, 5]  # 5
    student_two = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    student_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10

    counts = {1: 0, 2: 0, 3: 0}
    for index, answer in enumerate(answers):
        if answer == student_one[index % 5]:
            counts[1] += 1
        if answer == student_two[index % 8]:
            counts[2] += 1
        if answer == student_three[index % 10]:
            counts[3] += 1

    sorted_counts = sorted(counts.items(), key=lambda x: -x[1])
    answer = []
    max_count = 0
    for student, count in sorted_counts:
        if count >= max_count:
            answer.append(student)
            max_count = count
        else:
            break

    return answer

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42840
시간 : 9분 30초


다른 사람 풀이 :
========================================================================================
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
========================================================================================

노트 :
- 파이썬 itertools - count(), cycle(), repeat() 찾아보기
"""