def solution(array, commands):
    answer = []
    for command in commands:
        slice_array = array[command[0]-1:command[1]]
        slice_array.sort()
        answer.append(slice_array[command[2]-1])
    return answer


"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
시간 : 측정안함


다른 사람 풀이 :
========================================================================================
sorted 활용

def solution(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer
========================================================================================
map에 람다 활용

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
========================================================================================
배열 변수 세개에 할당

def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        result.append(sorted(array[i-1:j])[k-1])
    return result
========================================================================================

노트 :
파이썬 내장함수, 라이브러리 익숙해져야함

"""