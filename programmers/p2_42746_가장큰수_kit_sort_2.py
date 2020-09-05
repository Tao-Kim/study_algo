def str_with_dummy(number):
    number_str = str(number)
    size_of_str = len(number_str)
    remain_size = 6 - size_of_str

    if size_of_str < 6:
        number_str += number_str[0] * (6 - size_of_str)

    if number_str[0] > number_str[1]:
        return (number_str, -remain_size)
    else:
        return (number_str, remain_size)


def solution(numbers):
    numbers_tuple = [str_with_dummy(number) for number in numbers]
    numbers_tuple.sort(reverse=True)
    numbers_str = []

    for number_str, remain_size in numbers_tuple:
        remove_size = abs(remain_size)
        numbers_str.append(number_str[0:-remove_size])

    if len(numbers_str) == numbers_str.count('0'):
        return '0'
    else:
        return ''.join(numbers_str)

    """
    문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42746#
    시간 : 28


    다른 사람 풀이 :
    ========================================================================================
    - 람다 이용 비교
    
    - x * 3 원소의 크기가 0 < 원소 < 1000 이기때문
    - 12, 121 -> 121212 > 121121121
    - 21, 212 -> 212121 < 212212212

    - 마지막 str(int()) 를 통해 0000 처리

    def solution(numbers):
        numbers = list(map(str, numbers))
        numbers.sort(key=lambda x: x*3, reverse=True)
        return str(int(''.join(numbers)))
    ========================================================================================
    비교문을 직접 선언한 방식
    
    import functools

    def comparator(a,b):
        t1 = a+b
        t2 = b+a
        return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

    def solution(numbers):
        n = [str(x) for x in numbers]
        n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
        answer = str(int(''.join(n)))
        return answer
    ========================================================================================

    노트 :
    - 테스트 케이스를 미리 추가해서 풀이하기
    - 파이썬 sort에 key 파라미터 찾아보기 (functools.cmp_to_key 도)

    """