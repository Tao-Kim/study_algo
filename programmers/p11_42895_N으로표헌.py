
def solution(N, number):
    temp = [0,1,11,111,1111,11111,111111,1111111,11111111]
    number_dict = {i : set([N*temp[i]]) for i in range(1, 9)}
    
    def cal_all(pre_one, pre_two, cur):
        for pre_one_num in number_dict[pre_one]:
            for pre_two_num in number_dict[pre_two]:
                number_dict[cur].add(pre_one_num + pre_two_num)
                number_dict[cur].add(pre_one_num * pre_two_num)
                if pre_one_num // pre_two_num > 0:
                    number_dict[cur].add(pre_one_num // pre_two_num)
                if pre_two_num // pre_one_num > 0:
                    number_dict[cur].add(pre_two_num // pre_one_num)
                if pre_one_num - pre_two_num > 0:
                    number_dict[cur].add(pre_one_num - pre_two_num)
                if pre_two_num - pre_one_num > 0:
                    number_dict[cur].add(pre_two_num - pre_one_num)

    cal_all(1, 1, 2)
    
    cal_all(2, 1, 3)
    
    cal_all(3, 1, 4)
    cal_all(2, 2, 4)
    
    cal_all(4, 1, 5)
    cal_all(3, 2, 5)
    
    cal_all(5, 1, 6)
    cal_all(4, 2, 6)
    cal_all(3, 3, 6)
    
    cal_all(6, 1, 7)
    cal_all(5, 2, 7)
    cal_all(4, 3, 7)
    
    cal_all(7, 1, 8)
    cal_all(6, 2, 8)
    cal_all(5, 3, 8)
    cal_all(4, 4, 8)
    
       
    for num in range(1, 9):
        if number in number_dict[num]:
            return num
    
    return -1

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42895
시간 : 38분


다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
-
"""