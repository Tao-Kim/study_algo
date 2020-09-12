from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int):

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]



class Solution:
    def twoSum(self, nums: List[int], target: int):
        num_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in num_dict:
                return [num_dict[target - nums[i]], i]
            else:
                num_dict[nums[i]] = i

"""
문제주소 : https://leetcode.com/problems/two-sum/
시간 : 측정안함


다른 사람 풀이 :
========================================================================================

========================================================================================
노트 :
- 
"""