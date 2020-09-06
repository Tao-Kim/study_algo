import copy


def rotate_key(key):
    key_size = len(key)
    rotated_key = [[0] * key_size for _ in range(key_size)]
    
    for i in range(key_size):
        for j in range(key_size):
            rotated_key[key_size - 1 - j][i] = key[i][j]
            
    return rotated_key
    
    
    
def make_key_list(key):
    key_list = [key]
    
    key2 = rotate_key(key)
    key_list.append(key2)
    
    key3 = rotate_key(key2)
    key_list.append(key3)
    
    key4 = rotate_key(key3)
    key_list.append(key4)
    
    return key_list



def extend_lock(lock, empty_size):
    lock_size = len(lock)
    extended_lock = []
    extended_lock.extend([[0]*(lock_size + (2 * empty_size))]* empty_size)
    
    for row in lock:
        new_row = [0] * empty_size + row + [0] * empty_size
        extended_lock.append(new_row)
        
    extended_lock.extend([[0]*(lock_size + (2 * empty_size))]* empty_size)

    return extended_lock
    
    
    
def insert_key(extended_lock, key, x, y, empty_size):
    check_table = copy.deepcopy(extended_lock)
    key_size = len(key)

    for i in range(key_size):
        for j in range(key_size):
            check_table[x+i][y+j] += key[i][j]
                
    for i in range(empty_size, len(extended_lock) - empty_size):
        for j in range(empty_size, len(extended_lock) - empty_size):
            if check_table[i][j] != 1:
                return False
    
    return True
       
    
    
def solve_lock(extended_lock, key_list, empty_size):
    extended_lock_size = len(extended_lock)
    
    for i in range(0, extended_lock_size - empty_size):
            for j in range(0, extended_lock_size - empty_size):
                for key in key_list:
                    if insert_key(extended_lock, key, i, j, empty_size):
                        return True
                
    return False
    
    
    
def solution(key, lock):
    empty_size = len(key) - 1
    key_list = make_key_list(key)
    extended_lock = extend_lock(lock, empty_size)
    return solve_lock(extended_lock, key_list, empty_size)


"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/60059#
시간 : 74:27
테스트 : 38/38

- 1. 회전된 키를 모두 리스트로 갖고
- 2. lock 테이블은 열쇠가 들어갈 수 있는 모든 경우를 대비하여 확장하고
- 3. 모든 경우에 열쇠를 넣어 답이 되는지 체크함

다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
- p14 다른 사람 풀이 찾아보기
"""