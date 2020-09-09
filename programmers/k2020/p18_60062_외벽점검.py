import copy
n = None

def do_right_rotate(weaks, i, dist):
    sum = 0
    weaks_size = len(weaks)
    weaks_copy = copy.deepcopy(weaks)
    while sum < dist:
        if len(weaks_copy) == 0:
            break
        if i == weaks_size - 1:
            gap = weaks[0] + n - weaks[i]
        else:
            gap = weaks[i+1] - weaks[i]
        if gap + sum <= dist:
            sum += gap
            del weaks_copy[i]
            i = (i + 1) % weaks_size
            
    return weaks_copy


def do_left_rotate(weaks, i, dist):
    sum = 0
    weaks_size = len(weaks)
    weaks_copy = copy.deepcopy(weaks)
    while sum < dist:
        if len(weaks_copy) == 0:
            break
        if i == 0:
            gap = -(weaks[weaks_size - 1] - (weaks[i]+n))
        else:
            gap = -(weaks[i - 1] - weaks[i])
        if gap + sum <= dist:
            sum += gap
            del weaks_copy[i]
            i = (i - 1) % weaks_size
            
    return weaks_copy
            
min_count = 987654321
def do_all_case(weaks, dists, count):
    for i in range(len(weaks)):
        for j in range(len(dists)):
            count_after = count + 1
            dists_after = copy.deepcopy(dists)
            del dists_after[j]
            weaks_after = do_right_rotate(weaks, i, dists[j])
            if len(weaks_after) == 0:
                min_count = min(count_after, min_count)
            
            else:
                if len(dists_after) == 0:
                    continue
                else:
                    do_all_case(weaks_after, dists_after, count_after)
            
            weaks_after = do_left_rotate(weaks, i, dists[j])
            if len(weaks_after) == 0:
                min_count = min(count_after, min_count)
            
            else:
                if len(dists_after) == 0:
                    continue
                else:
                    do_all_case(weaks_after, dists_after, count_after)
            
            

def solution(_n, weaks, dists):
    global n
    n = _n

    
    do_all_case(weaks, dists, 0)
    
    return min_count

    
"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/60062
시간 : 못품 - 30분 풀고 시간 초과
테스트 : 시간 초과

- 5시간 측정 초과해서 다 못품, 다시 풀기

다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
- 다시풀기
"""